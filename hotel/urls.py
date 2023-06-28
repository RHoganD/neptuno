from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='index'),
    path('room_list', views.room_list , name='room_list'),
    path('<int:id>', views.room_details , name='room_details'),
    path('about', views.about , name='about'),
    path('contact', views.contact , name='contact'),
]