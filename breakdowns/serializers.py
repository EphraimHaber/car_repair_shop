from rest_framework import serializers
from .models import Worker, Car, Customer, Breakdown, TestAppointment


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

    def create(self, validated_data):
        return Worker(**validated_data)


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

    def create(self, validated_data):
        return Car(**validated_data)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        return Customer(**validated_data)


class BreakdownSerializer(serializers.ModelSerializer):
    assigned_worker = serializers.SlugRelatedField(read_only=True, slug_field='id')
    car_to_repair = serializers.SlugRelatedField(read_only=True, slug_field='id')

    class Meta:
        model = Breakdown
        fields = '__all__'

    def create(self, validated_data):
        return Breakdown(**validated_data)


class TestAppointmentSerializer(serializers.ModelSerializer):
    car_to_test = serializers.SlugRelatedField(read_only=True, slug_field='id')
    assigned_worker = serializers.SlugRelatedField(read_only=True, slug_field='id')

    class Meta:
        model = TestAppointment
        fields = ['id', 'car_to_test', 'bonus_points_on_fix', 'urgency', 'assigned_worker', 'is_fixed']

    def create(self, validated_data):
        return TestAppointment(**validated_data)
