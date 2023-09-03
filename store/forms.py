from django import forms
from .models import Product

class product_post_form(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','description','price','images','stock','category','is_available']