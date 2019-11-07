from django.urls import path
from . import views

urlpatterns = [
    path('', views.superhero_list, name='superhero_list'),
    path('heros/<int:pk>', views.superhero_detail, name='superhero_detail'),
    path('heros/new', views.superhero_create, name='superhero_create'),
    path('heros/<int:pk>', views.superhero_edit, name='superhero_edit'),
    path('heros/<int:pk>/delete', views.superhero_delete, name='superhero_delete'),
]