from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart, CartProduct
from .models import Order, OrderedProduct
from users.models import Profile
from home.models import Product
from django.core.paginator import Paginator

@login_required(login_url='login')
def checkout(request):
    cart,create= Cart.objects.get_or_create(user=request.user)
    cart_items = CartProduct.objects.filter(cart_id = cart.id)
    profile = Profile.objects.get(user = request.user)
    total_price = sum(cp.quantity * cp.product.discount_price for cp in cart_items)
    if request.method == "POST":
        order, create = Order.objects.get_or_create(user=request.user)
        for item in cart_items:
            orderedproduct = OrderedProduct(order=order, product=item.product)
            orderedproduct.save()
        cart_items.delete()
        return redirect('order_detail')
    return render(request, 'order\checkout.html', {"cart_products":cart_items , "profile": profile , 'total_price':total_price})

@login_required(login_url='login')
def checkout_item(request, product_id):
    product = Product.objects.get(id=product_id) 
    profile =  Profile.objects.get(user=request.user) 
    if request.method  == "POST":
        order, create =Order.objects.get_or_create(user = request.user)
        orderedproduct = OrderedProduct(order=order, product=product)
        orderedproduct.save()
        return redirect('order_detail')
    return render(request, 'order\checkout-item.html', {"product":product , "profile": profile , 'total_price':product.discount_price})


@login_required(login_url='login')
def order_detail(request):
    order, create = Order.objects.get_or_create(user=request.user)
    orders = OrderedProduct.objects.filter(order_id = order.id).order_by('-time')
    paginator = Paginator(orders, 5)
    page = request.GET.get('page')
    orders = paginator.get_page(page)
    return render(request, 'order\order_detail.html', { "orders":orders })