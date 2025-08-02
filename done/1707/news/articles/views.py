from django.shortcuts import render
from django.views.generic import TemplateView
from articles.data import articles
from articles.exceptions import CategoryNotFoundError
# http://127.0.0.1:8000/articles/sport/
# http://127.0.0.1:8000/articles/sport/olympic-star-breaks-world-record/

class CategoryView(TemplateView):
    template_name = "articles/index.html"

    def get_context_data(self, **kwargs):
        category_name = kwargs.get('category_name', None)
        if category_name not in articles:
            raise CategoryNotFoundError
        category_content = articles.get(category_name)
        return {
            "category_title": category_name,
            "category_content": category_content
        }

    def get(self, request, *args, **kwargs):
        try:
            context = self.get_context_data(**kwargs)
        except CategoryNotFoundError:
            return render(request, "main/404.html")
        return self.render_to_response(context)

class ArticleView(CategoryView):
    template_name = "articles/article.html"


    def get_context_data(self, **kwargs):
        category_data = super().get_context_data(**kwargs)
        article_slug = kwargs.get('article_slug')
        category_content = category_data.get('category_content')
        if article_slug not in category_content:
            raise CategoryNotFoundError
        article_content = category_content.get(article_slug)
        return category_data | {
            "article": article_content
        }