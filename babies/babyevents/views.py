from guardian.shortcuts import assign_perm
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from babyevents.serializers import ParentSerializer, BabySerializer, EventSerializer
from permissions.services import APIPermissionClassFactory
from babyevents.models import Parent, Baby, Event

def evaluate(user, obj, request):
    return user.username == obj.name

class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='ParentPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': False   ,
                },
                'instance': {
                    'retrieve': 'babyevents.view_parent',
                    'destroy': False,
                    'update': True,
                    'partial_update': 'babyevents.change_parent',
                    'events': 'babyevents.view_parent',
                    'babies': 'babyevents.view_parent'
                }
            }
        ),
    )
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
                    'list': False   ,
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
        parent = self.request.user
        pi = serializer.validated_data['pid']
        print('\n\n\n',Parent.objects.filter(pid = pi.pid)[0].name,'\n\n\n')
        print(parent)
        print('\n\n\n',str(parent)== str(Parent.objects.filter(pid = pi.pid)[0].name))
        if (str(parent)== str(Parent.objects.filter(pid = pi.pid)[0].name)):
            print("SI ENTRAMOOOOSO")
            baby = serializer.save()
            user = self.request.user
            assign_perm('babies.view_baby', user,baby)
            assign_perm('babies.change_baby', user, baby)
            return Response(serializer.data)
        return Response({
            'status':'Not authorized'
        })


def evaluate(user, obj, request):
    print(user,'\n\n HOLA \n\n')
    for x in Baby.objects.filter( pid__name = user.username):
        if(x.bid == request.bid):
            return True
    return False


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    permission_classes = (
        APIPermissionClassFactory(
            name='EventPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': False   ,
                },
                'instance': {
                    'retrieve': 'babyevents.view_event',
                    'destroy': False,
                    'update': True,
                    'partial_update': 'babyevents.change_event',
                    'events': evaluate
                }
            }
        ),
    )

    def perform_create(self, serializer):
        parent = self.request.user
        baby = Baby.objects.filter(name=serializer.validated_data['bid'])[0].pid.name
        print(' \n\n\n',parent)
        if (str(parent) == str(baby)):
            event = serializer.save()
            return Response(serializer.data)
        print('\n\n\nYa salimos\n\n\n')
        return Response({
            'status':'Not authorized'
        })
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
