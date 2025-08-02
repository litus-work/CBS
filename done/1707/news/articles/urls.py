from articles.views import CategoryView, ArticleView
from django.urls import path

urlpatterns = [
    path("<str:category_name>/", CategoryView.as_view(), name="category"),
    path("<str:category_name>/<slug:article_slug>/", ArticleView.as_view(), name="article"),
]