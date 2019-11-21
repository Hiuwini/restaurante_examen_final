from django.urls import include, path
from django.contrib import admin
from . import views
from django.conf.urls import include, url

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^menu/nuevo/$', views.new_menu, name='menu_nuevo'),
    path('menu/<int:pk>/', views.platos, name='platos'),
    ]
