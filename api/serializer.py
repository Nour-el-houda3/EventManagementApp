from rest_framework import serializer
from event.models import Event


class EventSerializer(serializer.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'