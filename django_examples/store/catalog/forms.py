from django import forms

from .models import Product


class ProductForm(forms.Form):

    name = forms.CharField(label='Nome')
    description = forms.CharField(
        label='Descrição', widget=forms.Textarea
    )
    quantity = forms.IntegerField(label='Quantidade')


class ProductModelForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'quantity', 'categories']
