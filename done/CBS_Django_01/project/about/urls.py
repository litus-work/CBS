from django.urls import path
from .views import about, about_team


urlpatterns = [
    path('', about),
    path('team/', about_team),
]