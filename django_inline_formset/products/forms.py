# 6th

from django import forms
from django.forms import inlineformset_factory

from .models import (
    Product, Image, Variant
)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'short_description': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
        }


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = '__all__'


class VariantForm(forms.ModelForm):

    class Meta:
        model = Variant
        fields = '__all__'
        widgets = {
            'size': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
        }


VariantFormSet = inlineformset_factory(
    Product, Variant, form=VariantForm,
    extra=0, can_delete=True,
    can_delete_extra=True
)
ImageFormSet = inlineformset_factory(
    Product, Image, form=ImageForm,
    extra=0, can_delete=True,
    can_delete_extra=True
)
