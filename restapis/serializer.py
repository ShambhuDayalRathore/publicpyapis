from rest_framework import serializers
from django.contrib.auth import get_user_model # add this


class DummySerializer(serializers.Serializer):
    zip = serializers.CharField(max_length=10)
    city = serializers.CharField(max_length=10)
    age = serializers.IntegerField()

    def __str__(self):
        return "Dummy Serializer Object"



        


