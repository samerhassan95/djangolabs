from django.contrib import admin  
from django.urls import path  
from . import views 
urlpatterns = [ 
    path('list',views.list),
    path('insert',views.insert),
    path('update',views.update),
    path('delete',views.delete),
               ]