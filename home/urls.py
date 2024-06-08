from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name = "index"),
    path('<int:id>/', views.detail, name='detail'),
    path('<str:cat>/',views.category_view, name='category')
]