from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from category.models import Category
from django.db.models import Q
from store.forms import product_post_form
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
# Create your views here.
def store(request,category_slug=None):
    print(category_slug)
    category=None
    products = None
    if category_slug :
        category = get_object_or_404(Category,slug=category_slug)
        products =Product.objects.filter(is_available=True,category=category)
    else:
        products =Product.objects.filter(is_available=True)
    categories = Category.objects.all()
    
   
    
    context ={'products':products,'categories':categories}
   
    return render(request,'store.html',context)


@login_required
def purchase_product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        # Process the purchase logic here
        # You can create an Order or perform any other required actions

        messages.success(request, f'You have successfully purchased {product.product_name}.')
    except Product.DoesNotExist:
        messages.error(request, 'Product not found.')

    return redirect('dashboard')

def product_detail(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e :
        raise e
    context ={
        'single_product' : single_product
    }  
    return render(request,'products_details.html',context) 

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'p_count': product_count,
    }
    return render(request, 'store.html', context)


def add_products(request):
   if request.method == 'POST':
        form = product_post_form(request.POST, request.FILES)
        if form.is_valid():
            product = form.save() 
            return redirect('store')
   else:
        form = product_post_form()
   return render(request,'post.html',{'form':form})


def editProduct(request,id):
    product = Product.objects.get(pk = id)
    form = product_post_form(instance = product)
    if request.method == 'POST':
        form = product_post_form(request.POST,instance = product)
        if form.is_valid():
            form.save()
            return redirect('store')
    return render(request,'post.html',{'form':form})

def delateProduct(request,id):
    book = Product.objects.get(pk = id).delete()
    return redirect('store')




