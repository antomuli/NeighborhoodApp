from rest_framework import serializers

from .models import Hood, Profile, Business, Department


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


class BusinessSerializer(serializers.ModelSerializer):
    business_name = serializers.CharField()
    description = serializers.CharField()
    business_email = serializers.CharField()

    class Meta:
        model = Business
        exclude = ['is_active', 'neighborhood', 'id', 'owner']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        exclude = ['neighborhood', 'id', 'is_active']
