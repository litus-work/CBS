from django.urls import path
from . import views

app_name = 'task_02'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('luke/', views.LukeView.as_view(), name='luke'),
    path('leia/', views.LeiaView.as_view(), name='leia'),
    path('han/', views.HanView.as_view(), name='han'),
]
