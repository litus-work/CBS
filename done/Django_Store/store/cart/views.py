from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from core.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib import messages


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        qty = cd['quantity']

        if product.stock <= 0:
            messages.error(request, 'Товар отсутствует на складе.')
            return redirect(request.META.get('HTTP_REFERER', 'cart:detail'))

        in_cart = cart.cart.get(str(product.id), {}).get('quantity', 0)
        final_qty = qty if cd['override'] else in_cart + qty

        if final_qty > product.stock:
            messages.error(request, f'Нельзя добавить больше, чем в наличии ({product.stock} шт).')
            return redirect(request.META.get('HTTP_REFERER', 'cart:detail'))

        cart.add(product, quantity=qty, override_quantity=cd['override'])
        messages.success(request, f'Товар «{product.name}» добавлен в корзину.')
    return redirect(request.META.get('HTTP_REFERER', 'cart:detail'))

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, f'Товар «{product.name}» удалён из корзины.')
    return redirect('cart:detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True,
        })
    return render(request, 'cart/detail.html', {'cart': cart})

@require_POST
def cart_clear(request):
    Cart(request).clear()
    messages.success(request, 'Корзина очищена.')
    return redirect('cart:detail')
