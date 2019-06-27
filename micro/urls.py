from django.urls import path

from . import views

app_name = 'micro'
urlpatterns = [
    path('', views.index, name='index'),
    path('send/', views.send, name='send'),
]