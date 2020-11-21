from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,
                              redirect, render)
from django.views.decorators.http import require_POST

from .filters import ProductFilter
from .forms import ProductForm
from .models import Product


def index(request):
    name = request.GET.get('name')
    if name:
        products = Product.objects.filter(name__icontains=name)
    else:
        products = Product.objects.all()
    context = { 'products': products }
    return render(request, 'products/home.html', context )

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Sua senha foi alterada com sucesso!')
            return redirect('homepage')
        else:
            messages.error(request, 'Por favor, corrija o erro abaixo.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})



@login_required
def list_products(request):
    user = request.user
    products = Product.objects.filter(seller=user)
    context = { 'products': products }
    return render(request, 'products/list.html', context )


@login_required
def new_product(request):
    if request.method=="POST":
        form = ProductForm(request.POST or None) 
        if form.is_valid():
            name = form.cleaned_data.get('name')
            price = form.cleaned_data.get('price')
            code = form.cleaned_data.get('code')
            quantity_in_stock = form.cleaned_data.get('quantity_in_stock')
            is_active = form.cleaned_data.get('is_active')
            seller = request.user
            new_product = Product(name=name,price=price, code=code, quantity_in_stock=quantity_in_stock, is_active=is_active, seller=seller)
            new_product.save()
            messages.success(request, 'Produto criado com sucesso!')
            return HttpResponseRedirect(redirect_to='/product/list/')
    else:
        form = ProductForm
        context = { 'form': form }
        return render(request, 'products/create.html', context )


@login_required
def edit_product(request, pk):
    product = Product.objects.filter(pk=pk,seller=request.user).get
    if not product:
        return redirect('404_page')
    context = { 'product': product }
    return render(request, 'products/update.html', context )


@login_required
@require_POST
def update_product(request, pk):
    product = Product.objects.filter(pk=pk,seller=request.user).first()
    if not product:
        return redirect('404_page')
    product_form = ProductForm(request.POST, instance=product or None)
    if product_form.is_valid():
        product_form.save()
    messages.success(request, 'Produto editado com sucesso!')
    return redirect('list_products')        


@login_required
@require_POST
def delete_product(request, pk):
    Product.objects.filter(pk=pk, seller=request.user).delete() 
    messages.success(request, 'Produto deletado com sucesso!')
    return redirect('list_products') 


def not_found(request):
    return render(request, 'products/404.html' )
