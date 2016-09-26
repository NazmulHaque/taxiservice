from rest_framework import serializers
from drivers.models import Driver


class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = ('id', 'name', 'phone', 'fare', 'kilometers_driven', 'car_type', 'car_number', 'has_ac',
                  'capacity', 'location', 'number_of_times_fined', 'total_fines', 'rating',
                  'created_at', 'modified_at')
