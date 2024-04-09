from rest_framework import serializers
from .models import User, Referral
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Include password field as write-only

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'referral_code']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # Hash the password
        return super().create(validated_data)

class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = ['referrer', 'referred_user', 'timestamp']
