from django.urls import path

from apps.posts.models import Post

from . import views

app_name = 'posts'

urlpatterns = [
    #path('', views.Index_Posts.as_view(), name='index_posts'),
    path('agregar/', views.Agregar_Post.as_view(), name='agregar_posts'),
    path('mis-posts/', views.Mis_Posts.as_view(), name='mis_posts'),

    path('post/ver/<int:pk>/', views.Ver_Post.as_view(), name='ver_post'),
    path('post/editar/<int:pk>/', views.Editar_Post.as_view(), name='editar_post'),
    path('post/delete/<int:pk>/', views.Delete_Post.as_view(), name='delete_post'),
]
