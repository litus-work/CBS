from django.urls import path
from .views import contact, contact_help


urlpatterns = [
    path('', contact),
    path('help/', contact_help),
]