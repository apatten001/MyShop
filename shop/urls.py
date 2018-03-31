from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path(r'^(?P<category_slug>[-\w]/$', views.product_list, name='product_list_by_category'),
    path('<int:pk>:<slug:slug>', views.product_detail, name='product_detail')
]