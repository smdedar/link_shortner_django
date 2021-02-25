from django.urls import path
from . import views
urlpatterns = [
    path('', views.link_shortner, name='link_shortner'),
    path('<str:alias>', views.link_redirect, name='link_redirect'),
]