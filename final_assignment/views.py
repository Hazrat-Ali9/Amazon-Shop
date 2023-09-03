from django.shortcuts import render,get_object_or_404
from store.models import Product
from category.models import Category

# Create your views here.
def home(request):
    return render(request,'index.html')
