

from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(request, category_slug=None):
    categories = Category.objects.prefetch_related('products__images')  # оптимизация
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = category.products.all()
    else:
        products = Product.objects.all()

    return render(request, 'core/product_list.html', {
        'categories': categories,
        'category': category,
        'products': products,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'core/product_detail.html', {'product': product})