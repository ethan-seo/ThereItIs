from django import forms

from .models import *

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('mainimage','sku','productname','productdesc','quantity','location','expiration_date')
        labels = {
            'mainimage':'Image:',
            'sku':'SKU:',
            'productname':'Product Name:',
            'productdesc':'Product Description:',
            'quantity':'Quantity:',
            'location':'Location:',
            'expiration_date':'Expiration Date:',
        }
