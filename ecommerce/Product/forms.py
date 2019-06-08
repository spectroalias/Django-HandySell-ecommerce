from .models import Comment
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['text']
        widget={
            'text':forms.Textarea()
        }
