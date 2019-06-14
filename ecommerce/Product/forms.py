from .models import Comment,Product
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['text']
        widget={
            'text':forms.Textarea()
        }

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