from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('session/', include('django.contrib.auth.urls')),
    path('change-password/', views.change_password, name='change_password'),
    path('product/list/', views.list_products, name='list_products'),
    path('product/create/', views.new_product, name='create_product'),
    path('product/edit/<int:pk>', views.edit_product, name='edit_product'),
    path('product/update/<int:pk>', views.update_product, name='update_product'),
    path('product/delete/<int:pk>', views.delete_product, name='delete_product'),
    path('not_found/', views.not_found, name='404_page')
]
