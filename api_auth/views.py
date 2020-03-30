from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import User
from v1.models import Profile
from .serializers import UserSerializer


class UserRegister(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            if User.objects.filter(email=serializer.validated_data['email']).first() is None:
                user = User(
                    first_name=serializer.validated_data['first_name'],
                    last_name=serializer.validated_data['last_name'],
                    email=serializer.validated_data['email'],
                    raw_password=serializer.validated_data['password']
                )
                user.save_user()
                gravatar_url = user.create_gravatar()
                user_profile = Profile(user=user, gravatar=gravatar_url)
                user_profile.save_profile()

                return Response(
                    {
                        'public_id': user.public_id,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'email': user.email,
                        'profile': {
                            'gravatar': user.profile.gravatar,
                            'bio': user.profile.bio
                        }
                    },
                    status=status.HTTP_201_CREATED)
                
            else:
                return Response(
                    {
                    'error': True,
                    'message': "User already exists"
                    },
                    status=status.HTTP_409_CONFLICT
                    )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)