from django.urls import path
from . import views
urlpatterns = [
    path('',views.store,name ='store'),
    path('category/<slug:category_slug>/',views.store,name ='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('purchase/<int:product_id>/', views.purchase_product, name='purchase_product'),
    path('search/', views.search, name='search'),
    path('details/',views.product_detail,name ='details'),
    path('add/',views.add_products,name ='add_product'),
    path('edit_product/<int:id>',views.editProduct,name='edit_product'),
    path('delete_product/<int:id>/',views.delateProduct,name='delete_product'),
]