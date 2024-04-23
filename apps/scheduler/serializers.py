from rest_framework import serializers

from apps.scheduler.models import Person, Aviability

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields =  "__all__"

class AviabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Aviability
        fields =  "__all__"