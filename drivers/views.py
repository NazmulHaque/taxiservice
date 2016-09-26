from rest_framework import generics
from rest_framework import filters

from drivers.models import Driver
from drivers.serializers import DriverSerializer


class DriverFilter(filters.FilterSet):
    class Meta:
        model = Driver
        fields = ['name', 'car_type', 'has_ac', 'capacity']


class DriverList(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_class = DriverFilter


class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
