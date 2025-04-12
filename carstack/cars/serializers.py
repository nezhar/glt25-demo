from rest_framework import serializers
from .models import Manufacturer, Feature, Car

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    features = FeatureSerializer(many=True)

    class Meta:
        model = Car
        fields = '__all__'
