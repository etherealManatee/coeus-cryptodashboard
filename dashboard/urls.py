from django import urls
from django.urls import path
from dashboard.views import *

app_name = "dashboard" #dashboard:

urlpatterns = [
    path("", dashboard_view, name="dashboard_view_page"),
    path("api/cryptocurrency/<str:crypto_name>", add_crypto, name="add_crypto"),
    path("refresh/", refresh_sidebar, name="refresh_sidebar")
]
