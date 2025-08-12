from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(request, category_slug=None):
    # здесь делаем ленивую выборку продуктов + картинок
    product_qs = Product.objects.prefetch_related('images').order_by('-created_at')
    categories = Category.objects.prefetch_related(
        Prefetch('products', queryset=product_qs)
    ).all()

    category = None
    products = Product.objects.all()
    if category_slug:
        category = Category.objects.prefetch_related('products__images').get(slug=category_slug)
        products = category.products.all()

    return render(request, 'core/product_list.html', {
        'categories': categories,
        'category': category,
        'products': products,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'core/product_detail.html', {'product': product})