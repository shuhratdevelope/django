from django.forms import model_to_dict
from django.shortcuts import render



from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Person
from .serializers import Poestserializers


class ListPoet(APIView):
    def get(self, request):
        lst = Person.objects.all().values()
        return Response({'Teacher': Poestserializers(lst, many=True).data})


    def post(self,requests):
        posts = Person.objects.create(
             name = requests.data['name'],
             content = requests.data['content'],
             cat_id = requests.data['cat_id'],
        )
        return Response({'posts': Poestserializers(posts).data})





#class ListPoet(APIView):
    #queryset = Person.objects.all()
    #serializer_class = Poestserializers
