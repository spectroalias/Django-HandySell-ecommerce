from .models import Product
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['title','description','price','image']
        widget={
            'description':forms.Textarea(),
            'price':forms.IntegerField(),
            'title':forms.TextInput(),
            'image':forms.URLField()

        }