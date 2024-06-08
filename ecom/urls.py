"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users import views as users_views
from django.contrib.auth import views as auth_views
from cart import views as cart_views
from order import views as order_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='users\login.html'), name='login'),
    path('register/', users_views.register, name='register'),
    path('profile/', users_views.profile, name = "profile"),
    path('logout/', users_views.logout_view, name='logout'),
    path('cart/', cart_views.cart_detail, name='cart_detail'),
    path('add-to-cart/<int:product_id>/', cart_views.add_to_cart, name='add_to_cart'), 
    path('remove-from-cart/<int:product_id>/', cart_views.remove_from_cart, name='remove_from_cart'),
    path('minus-from-cart/<int:product_id>/', cart_views.minus_from_cart, name= 'minus_from_cart'),
    path('edit-profile/', users_views.edit_profile, name='edit_profile'),
    path('orders/', order_views.order_detail, name='order_detail' ),
    path('checkout/', order_views.checkout, name='checkout'),
    path('checkout-item/<int:product_id>', order_views.checkout_item, name='checkout_item'),
    path('',include('home.urls')),

]
 