from django.urls import path
from . import views

# variable name must not be changed
urlpatterns = [path('', views.index, name='index'),
               path('about/', views.about, name='about')]
