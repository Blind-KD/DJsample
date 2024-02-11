from rest_framework import serializers
from userapp.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = '__all__'

class albumSerializer(serializers.ModelSerializer):
    class Meta:
        model = album
        fields = '__all__'

class photoSerializer(serializers.ModelSerializer):
    class Meta:
        model = photo
        fields = '__all__'