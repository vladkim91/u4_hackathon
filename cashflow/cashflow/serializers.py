from rest_framework import serializers
from .models import User, Influence


class InfluenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Influence
        fields = ('name', 'amount', 'date')


class UserSerializer(serializers.ModelSerializer):
    bills = InfluenceSerializer(
        many=True,
        read_only=True
    )
    transactions = InfluenceSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name',
                  'last_name', 'balance', 'bills', 'transactions')
