from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('foobar', views.foobar, name='foobar'),
    path('squared', views.squared, name='squared'),
]
