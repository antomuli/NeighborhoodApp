from rest_framework import serializers

from .models import Hood, Profile


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
        exclude = ['admin', 'assignee', 'id']
        read_only_fields = ['occupants', 'public_id']


class HoodInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hood
        exclude = ['id']


class HoodJoinSerializer(serializers.ModelSerializer):
    public_id = serializers.UUIDField()
    
    class Meta:
        model = Hood
        fields = ('public_id',)