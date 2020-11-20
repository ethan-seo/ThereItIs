from django import forms

from .models import *

class AddItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('sku','productname','productdesc','quantity','location','expiration_date')
