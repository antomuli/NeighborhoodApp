from rest_framework import serializers
from api_auth.models import Profile

from .models import Hood

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('gravatar', 'bio')


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(required=False)

    class Meta:
        model = Profile
        fields = ('gravatar', 'bio')


class HoodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hood
        exclude = ['admin', 'assignee']


class HoodInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hood
        fields = ('__all__')