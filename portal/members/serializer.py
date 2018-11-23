from rest_framework import serializers
from .models import attendance, profile
from django.contrib.auth.models import User


class ProfileBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = ('first_name', 'last_name', 'avatar')

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileBasicSerializer()
    class Meta:
        model = User
        fields = ('id', 'username', 'profile')
        depth = 1

class AttendanceSerializer(serializers.ModelSerializer):
    member = UserSerializer()
    class Meta:
        model = attendance
        fields = ('member','session_start','session_end')
