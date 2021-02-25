from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:slink>', views.link_destination, name='destination'),
]