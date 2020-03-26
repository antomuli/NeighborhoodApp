from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ..models import Hood
from..serializers import (
    HoodListSerializer, HoodInfoSerializer
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
            return Response(serializer.data, status=status.HTTP_200_OK)
             
        else:
            return Response({
                'error': True,
                'message': 'required parameter public_id'
            },
            status=status.HTTP_400_BAD_REQUEST
            )