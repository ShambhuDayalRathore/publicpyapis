from email import message
from pickle import NONE
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics


# Create your views here.
global data;
data = ["test value"]
class PersonView(APIView):

    def get(self, request, format=NONE):
        message = {
            "Respons":"200",
            "Message":"This is rest apis page",
            "data":data
        }
        return Response(message)

    def post(self, request, format=NONE):
        datam = request.data.get
        name  = datam.get("name")
        data.append(name)
        message = {
            "Respons":"200",
            "Message":"This is rest apis page",
            "data":data
        }
        return Response(message)

from . serializer import DummySerializer

class WatherView(generics.CreateAPIView):
    serializer_class = DummySerializer

    def create(self, request, *args, **kwargs):
        try:
            zip = request.data.get('zip')
            city = request.data.get('city')
            age = request.data.get('age')
            message = {
                "Respons":"400",
                "Message":"Something went wrong.",
                "zip":zip,
                "city":city,
                "age":age
            }
            return Response(message)

        except Exception as e:
            message = {
                "Respons":"400",
                "Message":"Something went wrong."
            }
            return Response(message)

  


    