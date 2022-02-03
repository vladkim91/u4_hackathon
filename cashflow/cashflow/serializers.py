from rest_framework import serializers
from .models import User, Influence


class InfluenceSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     read_only=True
    # )

    class Meta:
        model = Influence
        fields = ('name', 'amount', 'date')


class UserSerializer(serializers.ModelSerializer):
    bills = InfluenceSerializer(
        many=True,
        read_only=True
    )
    balance_history = InfluenceSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name',
                  'last_name', 'bills', 'balance_history')
