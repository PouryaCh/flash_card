from rest_framework import serializers
from django.contrib.auth.models import User

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}
        
        # def create(self, validated_data):
        #     user = User(
        #         username = validated_data['username'],
        #         email = validated_data['email']
                
        #     )
        #     user.set_password(validated_data['password'])
        #     user.save()
        #     return user
        
        
        # def update(self, instance, validated_data):
        #     instance.username = validated_data.get('username', instance.username)
        #     instance.email = validated_data.get('email', instance.email)
            
        #     password = validated_data.get('password', None)
        #     if password:
        #         instance.set_password(password)
                
        #     instance.save()
        #     return instance
        
        

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    
   
   
        
    

