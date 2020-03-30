from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from api_auth.models import User
from ..models import Profile

from ..serializers import UserProfileSerializer, UserProfileUpdateSerializer
from ..permissions import IsAuthenticatedProfile


class ProfileDisplayView(APIView):
    permission_classes = [IsAuthenticatedProfile]

    def get(self, request):
        if request.GET.get('public_id') is not None:
            user = User.objects.filter(public_id=request.GET.get('public_id')).first()
            user_profile = Profile.objects.filter(user=user).first()
            serializer = UserProfileSerializer(user_profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
             
        else:
            return Response({
                'error': True,
                'message': 'required parameter public_id'
            },
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request):
        serializer = UserProfileUpdateSerializer(data=request.data)
        current_user = request.user
        user_profile = Profile.objects.filter(user=current_user).first()
        if serializer.is_valid():
            user_profile.update_profile(
                bio=serializer.validated_data.get('bio', None)
            )
            return Response(serializer.data)
        
        return Response(serializer.errors)

