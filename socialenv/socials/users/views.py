from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer


# Create your views here.
class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        user_data = UserSerializer(users, many=True).data
        response_data = { "data": user_data }
        return Response(response_data, status = status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')

        User.objects.create(name=name, email=email, password=password)

        response_data = { "response": "item created" }
        return Response(response_data, status = status.HTTP_200_OK)

    def put(self, request):
        name = request.data.get('name')
        id = request.data.get('id')
        user = User.objects.filter(id=id).first()

        if user is None:
            response_data = { "response": "User does not exist" }
            return Response(response_data, status = status.HTTP_404_NOT_FOUND)

        user.name = name
        user.save()
        response_data = { "response": "Item updated" }
        return Response(response_data, status = status.HTTP_200_OK)

    def delete(self, request):
        
        user = User.objects.filter().first()
        if user is None:
            response_data = { "response": "User not found" }
            return Response(response_data, status = status.HTTP_404_NOT_FOUND)

        user.delete()
        response_data = { "response": "User deleted" }
        return Response(response_data, status = status.HTTP_200_OK)




