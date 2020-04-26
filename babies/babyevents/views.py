from guardian.shortcuts import assign_perm
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from babyevents.serializers import ParentSerializer, BabySerializer, EventSerializer
from permissions.services import APIPermissionClassFactory
from babyevents.models import Parent, Baby, Event

class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    
    @action(detail = True, methods=['get'])
    def babies(self, request , pk = None):
        parent = self.get_object()
        babies = Baby.objects.filter(pid=parent)
        return Response({
            'status':'ok',
            'Babies': (x.name for x in babies)
        })

def evaluar(user, obj, request):
    return user.username == obj.pid.name

class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer

    permission_classes = (
        APIPermissionClassFactory(
            name='BabyPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': 'babyevents.view_baby',
                    'destroy': False,
                    'update': True,
                    'partial_update': 'babyevents.change_baby',
                    'events': evaluar
                }
            }
        ),
    )

    @action(detail = True, methods = ['get'])
    def events(self, request, pk = None):
        baby = self.get_object()
        events = Event.objects.filter(bid = baby)
        return Response({
            'baby': baby.name,
            'status':'ok',
            'Events': ((x.etype + ": "+x.comment) for x in events)
        })

    def perform_create(self, serializer):
        self.pid = Parent.objects.filter(name = self.request.user)[0].pid
        baby = serializer.save()
        user = self.request.user
        assign_perm('babies.view_baby', user,baby)
        assign_perm('babies.change_baby', user, baby)
        return Response(serializer.data)

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    def perform_create(self, serializer):
        serializer.save()
        return Response(serializer.data)

    # @action(detail = True, methods=['post'])
    # def events(self, request, pk = None):
    #     # Necesita campos etype, comment, babyid
    #     newEvent = Event()
    #     newEvent.eid = Event.objects.all().order_by('-eid')[0] + 1
    #     newEvent.etype = request.etype
    #     newEvent.ecomment = request.comment
    #     newEvent.bid = Baby.objects.filter(bid = request.babyid)
    #     newEvent.save()

    #     return Response({
    #         'status': 'ok'
    #     })
