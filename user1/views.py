from rest_framework import serializers
from user1.models import user
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user1.serializers import UserSerializer
# Create your views here.
@api_view(['GET'])
def index(req):
    listUser = [
         {'name': "Nguyen A", 'email': "A@gmail.com", 'phone': "7141414141"}, 
         {'name': "Nguyen B", 'email': "B@gmail.com", 'phone': "8141174747"},
         {'name': "Nguyen C", 'email': "C@gmail.com", 'phone': "7575757774"}, 
         {'name': "Nguyen D", 'email': "D@gmail.com", 'phone': "5575774555"}, 
         {'name': "Nguyen E", 'email': "E@gmail.com", 'phone': "6555454545"}, 
         {'name': "Nguyen F", 'email': "F@gmail.com", 'phone': "7787878787"}, 
         {'name': "Nguyen G", 'email': "G@gmail.com", 'phone': "3989898989"}, 
         {'name': "Nguyen H", 'email': "H@gmail.com", 'phone': "8212121212"}, 
         {'name': "Nguyen I", 'email': "I@gmail.com", 'phone': "3010101440"}, 
         {'name': "Nguyen K", 'email': "K@gmail.com", 'phone': "2686868686"}
    ]
    return Response(listUser)

@api_view(['GET'])
def listUser(req):
    users = user.objects.all()
    serializers = UserSerializer(users, many=True)
    # dir(listUser)
    print(dir(listUser))
    return Response(serializers.data)   

@api_view(['GET'])
def DetailUser(req, key):
    detailUser = user.objects.get(id=key)
    serializers = UserSerializer(detailUser)
    return Response(serializers.data)


@api_view(['POST'])
def  createUser(req):
    serializer = UserSerializer(data=req.data)
    if serializer.is_valid() and serializer.data['name'] == 'teo':
        serializer.save()
        print(dir(serializer.data))
    return Response("abc")
    
@api_view(['PUT'])
def update_user(req, key):
    user_update = user.objects.get(id=key)
    serializers = UserSerializer(user_update, data=req.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def delete_user(req, key):
    user_delelte = user.objects.get(id=key)
    user_delelte.delete()
    return Response('Successfully')


