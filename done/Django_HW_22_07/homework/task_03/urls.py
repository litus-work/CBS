from django.urls import path
from .views import download_file

app_name = 'task_03'

urlpatterns = [
    path('', download_file, name='download'),
]
