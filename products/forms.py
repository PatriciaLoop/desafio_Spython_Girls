from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length = 100, required=True, label='', widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Insira o nome do produto'}))
    price = forms.DecimalField(min_value=0, required=True, label='', widget = forms.NumberInput(attrs={'class':'form-control','placeholder':'Insira o preço do produto'}))
    code = forms.IntegerField(min_value=0, required=True, label='', widget = forms.NumberInput(attrs={'class':'form-control','placeholder':'Insira o código do produto'}))
    quantity_in_stock = forms.IntegerField(min_value=0, required=True, label='', widget = forms.NumberInput(attrs={'class':'form-control','placeholder':'Insira a quantidade do produto'}))
    is_active = forms.BooleanField(required=False, label="Está ativo?")
    class Meta:
        model = Product
        fields = ('name', 'price', 'code', 'quantity_in_stock', 'is_active')
