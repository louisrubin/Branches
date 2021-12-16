from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.Inicio_Posts.as_view(), name='inicio_posts'),
    path('agregar/', views.Agregar_Post.as_view(), name='agregar_posts'),
]
