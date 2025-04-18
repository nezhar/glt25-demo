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
    manufacturer = ManufacturerSerializer(read_only=True)
    manufacturer_id = serializers.PrimaryKeyRelatedField(
        queryset=Manufacturer.objects.all(),
        source='manufacturer',
        write_only=True,
    )
    features = FeatureSerializer(many=True, read_only=True)
    features_ids = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(
            queryset=Feature.objects.all()
        ),
        write_only=True,
        source='features',
    )

    class Meta:
        model = Car
        fields = '__all__'
