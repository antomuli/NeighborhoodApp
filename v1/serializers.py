from rest_framework import serializers

from .models import Hood, Profile, Business, Department, Post


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


class PostSerializer(serializers.ModelSerializer):
    user_first_name = serializers.ReadOnlyField(source='user.first_name')
    user_last_name = serializers.ReadOnlyField(source='user.last_name')
    user_gravatar_url = serializers.ReadOnlyField(source='user.profile.gravatar')
    title = serializers.CharField(min_length=1)
    content = serializers.CharField(min_length=1)

    class Meta:
        model = Post
        exclude = ['neighborhood', 'id', 'user']
        read_only_fields = ['created_at', 'public_id']