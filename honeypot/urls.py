from django.urls import path
from .views import fake_admin_view

urlpatterns = [
    path("", fake_admin_view, name="honeypot_admin"),
]
