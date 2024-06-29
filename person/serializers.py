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



    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.content = validated_data.get("content", instance.content)
        instance.update_ad = validated_data.get("update_ad", instance.update_ad)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance





















   # class Meta:
    #    model =Person
       # fields = ('name', 'content')