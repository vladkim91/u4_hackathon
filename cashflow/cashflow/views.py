from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, InfluenceSerializer
from .models import User, Influence


def get_existing_user(username, password):
    return User.objects.get(username=username, password=password) if User.objects.filter(
        username=username, password=password) else None


class ProfileDetail(APIView):
    queryset = User.objects.all()

    def post(self, request, format=None):
        username = request.data.get("username") or ''
        password = request.data.get("password") or ''

        user = get_existing_user(username, password)

        res = 'None'
        if user != None:

            serializer = UserSerializer(user, )
            res = serializer.data

        return Response(res)


class CreateProfile(APIView):
    queryset = User.objects.all()

    def post(self, request, format=None):
        username = request.data.get("username") or ''
        password = request.data.get("password") or ''
        email = request.data.get('email') or ''
        first_name = request.data.get('first_name') or ''
        last_name = request.data.get('last_name') or ''
        balance = request.data.get('balance') or ''

        existing_user = get_existing_user(username, password)

        if existing_user != None:
            return Response('Not Available')

        new_user = self.queryset.create(username=username, password=password,
                                        email=email, first_name=first_name, last_name=last_name, balance=balance)

        serializer = UserSerializer(new_user)
        return Response(serializer.data)
