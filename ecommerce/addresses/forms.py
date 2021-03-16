from django import forms
from .models import Address,getcountry_choices

class AddressForm(forms.ModelForm):
    class Meta:
        model   = Address
        fields  = [
            'add_line_1',
            'add_line_2',
            'city',
            'pincode',
            'country'
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].widget.attrs['style']="width:100%;"