from django.shortcuts import render
from django.views.generic import TemplateView
from main.data import products
from main.exceptions import CategoryNotFoundError, ProductNotFoundError


class IndexView(TemplateView):
    template_name = "shop/index.html"

    def get_context_data(self, **kwargs):
        all_products = []
        for category_products in products.values():
            for slug, product in category_products.items():
                all_products.append(product | {"slug": slug})
        return {"products": all_products}


class CategoryView(TemplateView):
    template_name = "shop/category.html"

    def get_context_data(self, **kwargs):
        category_name = kwargs.get('category_name', None)
        if category_name not in products:
            raise CategoryNotFoundError
        category_products = products[category_name]
        return {
            "category_title": category_name,
            "products": [product | {"slug": slug} for slug, product in category_products.items()]
        }

    def get(self, request, *args, **kwargs):
        try:
            context = self.get_context_data(**kwargs)
        except CategoryNotFoundError:
            return render(request, "shop/404.html")
        return self.render_to_response(context)


class ProductDetailView(CategoryView):
    template_name = "shop/product_detail.html"

    def get_context_data(self, **kwargs):
        category_context = super().get_context_data(**kwargs)
        product_slug = kwargs.get('product_slug')
        category_name = kwargs.get('category_name')
        category_products = products.get(category_name)

        if not category_products or product_slug not in category_products:
            raise ProductNotFoundError

        product = category_products[product_slug]
        return category_context | {"product": product}
