from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ..models import Hood
from..serializers import (
    HoodListSerializer, HoodInfoSerializer, HoodJoinSerializer
)


class HoodList(APIView):
    def get(self, request):
        all_hoods = Hood.objects.all()
        serializer = HoodListSerializer(all_hoods, many=True)
        return Response({
            'total': len(all_hoods),
            'results': serializer.data
        })


class HoodInfo(APIView):
    def get(self, request):
        if request.GET.get('public_id') is not None:
            hood = Hood.objects.filter(public_id=request.GET.get('public_id')).first()
            serializer = HoodInfoSerializer(hood)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
                )
             
        else:
            return Response({
                'error': True,
                'message': 'required parameter public_id'
            },
            status=status.HTTP_400_BAD_REQUEST
            )


class HoodCreateView(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)

    def post(self, request):
        serializer = HoodListSerializer(data=request.data)

        if serializer.is_valid():
            existing_hood = Hood.objects.filter(
                hood_name = serializer.validated_data['hood_name'],
                location = serializer.validated_data['location']
            ).first()

            if existing_hood is None:
                new_hood = Hood(
                    hood_name=serializer.validated_data['hood_name'],
                    location=serializer.validated_data['location'],
                    admin=request.user
                )
                new_hood.save_hood()
                return Response(
                    {
                        "public_id": new_hood.public_id,
                        "hood_name": new_hood.hood_name,
                        "location": new_hood.location,
                        "occupants": new_hood.occupants,
                        "admin_public_id": new_hood.admin.public_id,
                    },
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response({
                    'error': True,
                    'message': 'Another hood with that location and name exists'
                },
                status=status.HTTP_409_CONFLICT
                )

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class JoinHoodView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = HoodJoinSerializer(data=request.data)
        current_user = request.user

        if serializer.is_valid():
            hood = Hood.objects.filter(
                public_id=serializer.validated_data.get('public_id')
            ).first()
            
            if hood is not None:
                current_user.profile.neighborhood = hood
                current_user.profile.save_profile()

                hood.occupants += 1
                hood.save_hood()

                return Response(
                    serializer.data
                )
            
            else:
                return Response({
                    "error": True,
                    "message": "Neighborhood does not exist"
                },
                status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )