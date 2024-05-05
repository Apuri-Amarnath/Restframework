from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Cab, Booking


class CabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cab
        fields = ['id', 'cab_number', 'driver_name', 'location', 'is_available', 'created_at', 'updated_at']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'cab', 'pickup_location', 'destination', 'pickup_time', 'booking_time']
        extra_kwargs = {'user': {'read_only': True}}

    user = serializers.StringRelatedField()
    cab = CabSerializer()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True,'style': {'input_type': 'password'}}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
