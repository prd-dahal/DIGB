"""Library Imports"""
from rest_framework import generics
from rest_framework import permissions

"""Local Imports"""
from digb_backend.TaxInformation.models import ProgressBarModel
from digb_backend.TaxInformation.v1.serializers import ProgressBarSerializer

class ProgressBarListView(generics.ListAPIView):
    """
    This base queryset only returns the data which are not archived.
    This helps to obtain the soft delete
    """
    queryset = ProgressBarModel.objects.unarchived()
    serializer_class = ProgressBarSerializer
    permission_classes = [permissions.AllowAny]
