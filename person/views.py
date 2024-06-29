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
        serializers = Poestserializers(data=requests.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response({'posts': serializers.data})


    def put(self,requests, *args, **kwargs):
        pk = kwargs.get("pk", None )
        if not pk:
            return Response({"post": "Method put not allowed"})


        try:
            instance = Person.objects.get(pk=pk)
            instance.save()
        except:
            return Response({"post": "object not found"})

        serializers = Poestserializers(data=requests.data, instance=instance)
        serializers.is_valid(raise_exception=True)
        return Response({"post": serializers.data})

    def patch(self,requests, *args, **kwargs):
        pk = kwargs.get("pk", None )
        if not pk:
            return Response({"post": "Method put not allowed"})


        try:
            instance = Person.objects.get(pk=pk)
            instance.save()
        except:
            return Response({"post": "object not found"})

        serializers = Poestserializers(data=requests.data, instance=instance, partial=True)
        serializers.is_valid(raise_exception=True)
        return Response({"post": serializers.data})


    def delete(self, *agrs, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"post": "Method put not allowed"})

        try:
            instance = Person.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({"post": "object not found"})

        serializers = Poestserializers(instance=instance)
        return Response({"answer": f"Deleted ID - {pk}"})



       # posts = Person.objects.create(
        #     name = requests.data['name'],
         #    content = requests.data['content'],
           #  cat_id = requests.data['cat_id'],
        #)




#class ListPoet(APIView):
    #queryset = Person.objects.all()
    #serializer_class = Poestserializers
