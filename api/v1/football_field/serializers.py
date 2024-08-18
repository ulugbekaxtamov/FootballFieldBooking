from rest_framework import serializers

from api.v1.user.serializers import UserSerializer
from apps.football_field.models import FootballField, FootballFieldImage


class FootballFieldImageImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballFieldImage
        fields = ['id', 'image']


class FootballFieldSerializer(serializers.ModelSerializer):
    images = FootballFieldImageImageSerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True)
    distance = serializers.FloatField(read_only=True)

    class Meta:
        model = FootballField
        fields = [
            'id', 'name', 'address', 'contact', 'price_per_hour',
            'latitude', 'longitude', 'images', 'distance'
        ]
