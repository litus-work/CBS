from django.urls import path
from .views import catalog, product, info


urlpatterns = [
    path('', catalog),
    path('product/', product),
    path('info/', info),
]