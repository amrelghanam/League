from rest_framework import serializers
from django.contrib.auth.models import User
#from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True}
        }


    def validate_password(self, value):
        if len(value) > 8:
            raise serializers.ValidationError( "Password must not exceed 8 characters.")
        return value
   

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }