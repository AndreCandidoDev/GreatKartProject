from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


# usa a session id para criar o carrinho
def _cart_id(request):  # private function
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id): # adiciona item ao carrinho e adiciona quantidade
    product = Product.objects.get(id=product_id)  # pega o produto pelo id
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))  # busca o carrinho pela session da request
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1  # soma 1 na quantidade de produto
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart')


def remove_cart(request, product_id):  # diminui a quantidade no carrinho
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def remove_cart_item(request, product_id):  # remove o item do carrinho
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')


def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += cart_item.product.price * cart_item.quantity
            quantity += cart_item.quantity
        tax = (2*total)/100  # aplicar regra de imposto correta aki
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass  # ignora
    context = {'total': total,
               'quantity': quantity,
               'cart_items': cart_items,
               'tax': tax,
               'grand_total': grand_total,
    }
    return render(request, 'store/cart.html', context)