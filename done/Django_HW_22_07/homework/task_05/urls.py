from django.urls import path
from .views import todo_view

urlpatterns = [
    path("", todo_view, name="todo_sorted"),
]
