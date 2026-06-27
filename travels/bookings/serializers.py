from rest_framework import serializers
from .models import Bus, Seat

class BusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields ='__all__'

class SeatSerializers(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id','seat_number','is_booked']