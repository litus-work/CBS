from django.urls import path
from . import views

urlpatterns = [
    path("text/", views.text_view, name="text_view"),
    path("html/", views.html_view, name="html_view"),
    path("json/", views.json_view, name="json_view"),
    path("file/", views.file_view, name="file_view"),
]
