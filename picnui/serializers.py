from rest_framework import serializers
from .models import Routine
from djongo import models


class RoutineSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=150, min_length=5)
    capturedBy = serializers.CharField(max_length=150, min_length=5)

    class Meta:
        model = Routine
        fields = ['name', 'capturedBy','points']

    # def validate(self, attrs):
    #     name = attrs.get('name', '')
    #     if Routine.objects.filter(name=name).exists():
    #         raise serializers.ValidationError(
    #             {'name': ('name is already in use')})
    #     return super().validate(attrs=attrs)
    #
    # def create(self, validated_data):
    #     return Routine.objects.create_routine(**validated_data)