from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = skill
        fields = ('name', 'type')

class PortalSerializer(serializers.ModelSerializer):
    class Meta:
        model = portal
        fields = ('name',)


class SocialProfilesSerializer(serializers.HyperlinkedModelSerializer):
    portal = serializers.ReadOnlyField(source='portal.name')
    class Meta:
        model = social_profiles
        fields = ('portal', 'link',)

class ProfileBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = ('first_name', 'last_name', 'avatar')

class UserBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
        depth = 1

class ProfileSerializer(serializers.ModelSerializer):
    interests = SkillSerializer(many=True)
    expertise = SkillSerializer(many=True)
    user = UserBasicSerializer()
    class Meta:
        model = profile
        fields = ('first_name', 'last_name', 'email', 'avatar', 'bio', 'location', 'typing_speed', 'birthday', 'interests', 'expertise', 'links', 'user' )

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileBasicSerializer()
    class Meta:
        model = User
        fields = ('id', 'username', 'profile')

class AttendanceSerializer(serializers.ModelSerializer):
    member = UserSerializer()
    class Meta:
        model = attendance
        fields = ('member','session_start','session_end','duration')

class UserAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = attendance
        fields = ('session_start','session_end','duration')

class DateAttendanceSerializer(serializers.ModelSerializer):
    member = UserSerializer()
    class Meta:
        model = attendance
        fields = ('member','duration')

class ResponsibilitySerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)
    class Meta:
        model = responsibility
        fields = ('id','title', 'about','thread','members')

class UserResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = responsibility
        fields = ('id', 'title')