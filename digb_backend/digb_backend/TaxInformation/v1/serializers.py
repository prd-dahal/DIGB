"""Library Imports"""
from rest_framework import serializers
"""Local Imports"""
from digb_backend.TaxInformation.models import ProgressBarModel


class ProgressBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressBarModel
        fields = ['title', 'subtitle', 'order', 'content']
