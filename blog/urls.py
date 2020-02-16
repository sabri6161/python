from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('ilk_fonksiyon', views.ilk_fonksiyon, name='ilk_fonksiyon'),
]