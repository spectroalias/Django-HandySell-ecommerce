from .models import Product
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['title','description','price','image']
        widget={
            'title':forms.TextInput(),
            'description':forms.Textarea(),
            'price':forms.IntegerField(),
            'image':forms.URLField()
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['style']="color:black;"
        self.fields['price'].widget.attrs['style']="color:black;width:100%"
        self.fields['title'].widget.attrs['style']="color:black;width:100%"
        self.fields['image'].widget.attrs['style']="color:black;width:100%"