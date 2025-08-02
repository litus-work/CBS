from main.views import IndexView, CategoryView, ProductDetailView
from django.urls import path

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<str:category_name>/", CategoryView.as_view(), name="category"),
    path("<str:category_name>/<slug:product_slug>/", ProductDetailView.as_view(), name="product_detail"),
]