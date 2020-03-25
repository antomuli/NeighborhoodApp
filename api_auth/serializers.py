from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        label='Email',
        required=True,
        allow_blank=False,
        allow_null=False
    )

    class Meta:
        model = User
        fields = ('public_id', 'email', 'first_name', 'last_name', 'password')
        read_only_fields = ['public_id']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True},
        }

