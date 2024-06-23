from requests import Response
from rest_framework import serializers
from rest_framework.response import Response

from .models import Person

class Poestserializers(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    content = serializers.CharField()
    creatd_ad = serializers.DateTimeField(read_only=True)
    update_ad = serializers.DateTimeField(read_only=True)
    is_poblshd = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()





















   # class Meta:
    #    model =Person
       # fields = ('name', 'content')