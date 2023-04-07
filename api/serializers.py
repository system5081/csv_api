from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Csv

class UserSerializer(serializers.ModelSerializer):

    class Meta :
        model =get_user_model()
        fields =('email','password','username','id')
        extra_kwargs ={'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)

        return user

class CsvSerializer(serializers.ModelSerializer):

    class Meta:
        model = Csv
        fields = ['id','title','csv']