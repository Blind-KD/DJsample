from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from userapp.models import *
from .serializers import *
from django.contrib.auth.models import User

@api_view(['GET'])
def userAlbumAPI(request, name):
    data = User.objects.get(username=name)
    dd = album.objects.filter(author=data)
    serializers = albumSerializer(dd, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def albumAPI(request):
    data = album.objects.all().order_by('-dateTime')
    serializers = albumSerializer(data, many=True)
    return Response(serializers.data)