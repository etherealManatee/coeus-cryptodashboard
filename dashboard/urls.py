from django import urls
from django.urls import path
from dashboard.views import *

app_name = "dashboard" #dashboard:

urlpatterns = [
    path("", dashboard_view, name="dashboard_view_page")
]
