from django.urls import path
from . import views
urlpatterns = [
    path('',views.register,name ='register'),
    path('profile/',views.profile,name ='profile'),
    path('login/',views.login_user,name ='login'),
    path('logout/', views.logout_user, name='logout'),
]
