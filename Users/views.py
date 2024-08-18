from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
# from . models import Users
from rest_framework import viewsets
from . serilizer import UsersSerializers, LoginSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication  import TokenAuthentication
from rest_framework.authentication import authenticate
from rest_framework import status
from rest_framework import viewsets

class RegisterUserView(APIView):
    
    def post(self, request):
        serializer = UsersSerializers
        
        req_data = request.data
        
        serializer = UsersSerializers(data=req_data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        
        user_data = User(
            username = data["username"],
            email=data["email"]
        )
        user_data.set_password(data["password"])
        user_data.save()
        
        return Response(serializer.data)
        
        

    
    # user = User(username='hamid', email='')
    # user.set_password('1912')  
    # user.save()
    

class LoginUserView(APIView):
    serializer_class = LoginSerializer
    # authentication_classes = [TokenAuthentication]
    
    def post(self, request):
        serializer = LoginSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'success': 'Login Successfully'}, status=status.HTTP_200_OK)
            return Response({'message': 'Invalid Username or Password'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class UserListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializers





















