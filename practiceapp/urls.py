from django.urls import path
from . import views

urlpatterns = [
    path('', views.superhero_list, name='superhero_list'),
     path('heros/<int:pk>', views.superhero_detail, name='superhero_detail'),
]