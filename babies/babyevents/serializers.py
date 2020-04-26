from rest_framework import serializers

from .models import Parent
from .models import Baby
from .models import Event

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ('pid', 'name')

class BabySerializer(serializers.ModelSerializer):
    class Meta:
        model = Baby
        fields = (
            'bid',
            'name',
            'pid'
        )

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'eid',
            'etype',
            'comment',
            'bid'
        )