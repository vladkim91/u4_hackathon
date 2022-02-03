from rest_framework import serializers
from .models import User, Influence


class UserSerializer(serializers.HyperlinkedModelSerializer):
    bills = serializers.HyperlinkedRelatedField(
        view_name='influence_detail',
        lookup_field='bills',
        many=True,
        read_only=True
    )
    balance_history = serializers.HyperlinkedRelatedField(
        view_name='influence_detail',
        lookup_field='balance_history',
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name',
                  'last_name', 'bills', 'balance_history',)


class InfluenceSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='profile_detail',
        read_only=True
    )

    class Meta:
        model = Influence
        fields = ('name', 'amount', 'date', 'user',)
