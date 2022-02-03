from rest_framework import generics
from .serializers import UserSerializer, InfluenceSerializer
from .models import User, Influence


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class InfluenceList(generics.ListCreateAPIView):
    queryset = Influence.objects.all()
    serializer_class = InfluenceSerializer


class InfluenceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Influence.objects.all()
    serializer_class = InfluenceSerializer
