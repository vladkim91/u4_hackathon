from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, InfluenceSerializer
from .models import User, Influence
from datetime import datetime


def get_existing_user(username, password):
    return User.objects.get(username=username, password=password) if User.objects.filter(
        username=username, password=password) else None


class Login(APIView):
    queryset = User.objects.all()

    def post(self, request, format=None):
        incoming_username = request.data.get('username') or ''
        password = request.data.get('password') or ''
        user = get_existing_user(incoming_username, password)
        if user == None:
            return Response('Failed!')

        serializer = UserSerializer(user)

        return Response(serializer.data['id'])


class ProfileDetail(APIView):
    queryset = User.objects.all()

    def post(self, request, format=None):
        user_pk = int(request.data.get('user')) or None

        user = self.queryset.filter(id=user_pk).first()

        if user == None:
            return Response('Failed!')

        serializer = UserSerializer(user)
        print(serializer.data)
        user_info = {
            'username': serializer.data['username'],
            'first_name': serializer.data['first_name'],
            'last_name': serializer.data['last_name'],
            'email': serializer.data['email'],
            'balance': serializer.data['balance'],
            'bills': serializer.data['bills'],
            'transactions': serializer.data['transactions']
        }

        return Response(user_info)


class CreateProfile(APIView):
    queryset = User.objects.all()

    def post(self, request, format=None):
        username = request.data.get('username') or ''
        password = request.data.get('password') or ''
        email = request.data.get('email') or ''
        first_name = request.data.get('first_name') or ''
        last_name = request.data.get('last_name') or ''
        balance = request.data.get('balance') or 0

        existing_user = get_existing_user(username, password)

        if existing_user != None:
            return Response('Failed!')

        new_user = self.queryset.create(username=username, password=password,
                                        email=email, first_name=first_name, last_name=last_name, balance=balance)

        serializer = UserSerializer(new_user)
        return Response(serializer.data)


class CreateBill(APIView):
    queryset = Influence.objects.all()

    def post(self, request, format=None):
        user_pk = int(request.data.get('id')) or None

        user = User.objects.get(id=user_pk) if User.objects.filter(
            id=user_pk) else None

        if user_pk == None or user == None:
            return Response('Failed!')

        name = request.data.get('name') or ''
        amount = request.data.get('amount') or 0
        amount = int(amount)
        new_bill = self.queryset.create(name=name, amount=amount, bills=user)
        serializer = InfluenceSerializer(new_bill)
        return Response(serializer.data)


class UpdateBill(APIView):
    queryset = Influence.objects.all()

    def put(self, request, format=None):
        influence_pk = int(request.data.get('id')) or None
        info = request.data
        influence = self.queryset.filter(id=influence_pk)
        print(info)

        update_result = influence.update(
            name=info['name'], amount=info['amount'])

        if update_result == 0:
            return Response('Failed!')

        serializer = InfluenceSerializer(influence.first())
        return Response(serializer.data)


class DeleteBill(APIView):
    queryset = Influence.objects.all()

    def delete(self, request, pk, format=None):
        influence_pk = pk
        influence = self.queryset.filter(id=influence_pk)
        delete_result = influence.delete()

        if delete_result == 0:
            return Response('Failed!')

        return Response('Success!')


class CreateTransaction(APIView):
    queryset = Influence.objects.all()

    def post(self, request, format=None):
        user_pk = int(request.data.get('user')) or None

        user = User.objects.get(id=user_pk) if User.objects.filter(
            id=user_pk) else None

        if user_pk == None or user == None:
            return Response('Failed!')

        name = request.data.get('name') or ''
        amount = int(request.data.get('amount')) or 0
        date = datetime.now().date()
        new_bill = self.queryset.create(
            name=name, amount=amount, transactions=user, date=date)
        serializer = InfluenceSerializer(new_bill)
        return Response(serializer.data)
