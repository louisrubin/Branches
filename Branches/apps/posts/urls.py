from django.urls import path

from . import views
from .views import *

app_name = "posts"

urlpatterns = [
    path('', views.Inicio_Posts.as_view(), name='inicio_posts'),
    path('agregar/', AgregarPost.as_view(), name='agregar_posts'),
]
