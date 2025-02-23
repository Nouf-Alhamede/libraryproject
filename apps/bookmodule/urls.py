from django.urls import path
from . import views
urlpatterns = [
    path('<int:bookId>/', views.viewbook),
    path('', views.index),
    path('index2/<val1>/', views.index2),
    
]

