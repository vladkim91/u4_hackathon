from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, InfluenceSerializer
from .models import User, Influence


class UserDetail(APIView):
    queryset = User.objects.all()

    def get(self, request, format=None):
        return Response(request.data)
