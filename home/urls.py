from django.urls import path
from .import views 
app_name = 'home'
urlpatterns = [
    path('', views.index),
    path('detail/<int:id>', views.detail, name='detail'),
    path('shoppingcart/', views.shoppingcart, name ='cart'),
]