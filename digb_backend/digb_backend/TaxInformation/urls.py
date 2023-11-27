"""Library Imports"""
from django.urls import path

"""Local Imports"""
from digb_backend.TaxInformation.v1.views import ProgressBarListView

urlpatterns = [
    path('progressbar/', ProgressBarListView.as_view(), name="progress-bar-list"),
]
