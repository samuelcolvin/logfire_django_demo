from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_fish, name='index'),
    path('add/', views.add_fish, name='add'),
]
