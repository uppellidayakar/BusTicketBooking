from rest_framework import serializers
from .models import Bus, Seat
from django.contrib.auth.models import User

class UserRegisterSearializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        models = User
        fields = ['username', 'email', 'password']

    def create(self, validate_date):
        user = User.objects.create_user(
            username = validate_date['username'],
            email = validate_date['email'],
            password = validate_date['password']
        )
        return user
    
class BusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields ='__all__'

class SeatSerializers(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id','seat_number','is_booked']