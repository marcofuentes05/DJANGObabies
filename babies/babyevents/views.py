from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from babyevents.serializers import ParentSerializer, BabySerializer, EventSerializer

from babyevents.models import Parent, Baby, Event


def l0(request):
    queryset = Event.objects.get(eid=1)
    serializer = EventSerializer(queryset)
    return Response(serializer.data)
# class ParentViewSet(viewsets.ViewSet):
    

#     queryset = Parent.objects.all()

#     def list(self, request):
#         serializer = ParentSerializer(self.queryset)
#         return Response(serializer.data)