from rest_framework import serializers
from .models import User, Influence


class UserSerializer(serializers.HyperlinkedModelSerializer):
    bills = serializers.HyperlinkedRelatedField(
        view_name='profile_detail',
        many=True
    )
    balance_history = serializers.HyperlinkedRelatedField(
        view_name='profile_detail',
        many=True
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name',
                  'last_name', 'bills', 'balance_history',)


class InfluenceSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='profile_detail'
    )

    class Meta:
        model = Influence
        fields = ('name', 'amount', 'date')
