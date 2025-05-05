
from django.contrib import admin 
from django.urls import path
from . views import register,CustomLoginView #  لي lohin تم اضافتها 
from django.contrib.auth.views import LogoutView # تم اضافتها لي login out
urlpatterns = [
 path('register/', register, name="register"), 
 path('login/', CustomLoginView.as_view(), name="login"),# CustomLoginView هذي فنكشن موجوده في الجانقو راح نستعملها 
path('logout/', LogoutView.as_view(), name="logout"),
]