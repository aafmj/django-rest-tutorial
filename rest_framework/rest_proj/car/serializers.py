from rest_framework import serializers
from .models import Person, Car


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarReadSerializer(serializers.ModelSerializer):
    # person = PersonSerializer()

    class Meta:
        model = Car
        fields = '__all__'
        depth = 5
