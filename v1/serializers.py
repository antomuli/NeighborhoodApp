from rest_framework import serializers
from api_auth.models import Profile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('gravatar', 'bio')


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(required=False)

    class Meta:
        model = Profile
        fields = ('gravatar', 'bio')