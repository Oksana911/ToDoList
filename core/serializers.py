from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from core.models import User


class SignUpSerializer(serializers.ModelSerializer):
    password_repeat = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password_repeat']

    def validate_password(self, data):
        validate_password(data)
        return data

    def validate_password_repeat(self, data):
        if data != self.initial_data.get("password"):
            raise serializers.ValidationError("Введенные пароли не совпадают")
        return data

    def create(self, validated_data):
        del validated_data['password_repeat']
        user = User.objects.create_user(**validated_data)
        return user
