from django.shortcuts import render
from django.core.paginator import Paginator 
from .models import Product
# Create your views here.

def index(request):
    products = Product.objects.all().order_by('name')
    paginator = Paginator(products,8)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    search = request.GET.get('search_item')
    flag = False
    if search is not None and search != '':      
        products = Product.objects.filter(name__icontains = search) 
        flag = True
    return render(request, 'home/index.html', {"products":products, "search_flag":flag} )

def detail(request,id):
    product = Product.objects.get(id=id)
    return render(request, 'home/detail.html', {"product":product})


def category_view(request, cat):
    products = Product.objects.filter(category = cat).order_by('name')
    return render(request, 'home/category.html', {'products':products, "category":cat})