from django.shortcuts import redirect, render
from .models import Cart, CartProduct
from home.models import Product
from django.contrib.auth.decorators  import login_required

@login_required
def cart_detail(request):
    cart,create = Cart.objects.get_or_create(user = request.user)
    cart_products = CartProduct.objects.filter(cart_id = cart.id)
    total_price = sum(cp.quantity * cp.product.discount_price for cp in cart_products)
    return render(request, 'cart/cart_detail.html', {'cart_products': cart_products, 'total_price': total_price})

@login_required
def add_to_cart(request,product_id):
    cart, create = Cart.objects.get_or_create(user = request.user)
    product = Product.objects.get(id = product_id)
    cart_product, create = CartProduct.objects.get_or_create(cart=cart,product=product)
    if not create:
        cart_product.quantity += 1
    cart_product.save()
    return redirect('cart_detail')

@login_required
def minus_from_cart(request,product_id):
    cart = Cart.objects.get(user = request.user)
    product = Product.objects.get(id = product_id)
    cart_product = CartProduct.objects.get(cart=cart,product=product)
    cart_product.quantity -= 1
    if cart_product.quantity>0:
        cart_product.save()
    else:
        cart_product.delete()
    return redirect('cart_detail')

@login_required
def remove_from_cart(request,product_id):
    cart = Cart.objects.get(user=request.user)
    product = Product.objects.get(id=product_id)
    cart_product = CartProduct.objects.get(product_id=product_id, cart_id=cart.id)
    cart_product.delete()
    return redirect('cart_detail')
    