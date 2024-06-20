from rest_framework import serializers
from .models import Person

class Poestserializers(serializers.ModelSerializer):
    class Meta:
        model =Person
        fields = ('name', 'content')