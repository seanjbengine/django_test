from django.urls import path
from schooler import views

urlpatterns = [
    path('', views.index, name='index')
]
