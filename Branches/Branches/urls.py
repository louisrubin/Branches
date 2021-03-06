"""ejemplo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views     # importo el archivo views.py que creamos 
from django.contrib.auth import views as auth

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    #path('', views.inicio, name = 'inicio'),     # views. + (funcion en el archivo 'views.py' que retorna un render)
    path('login/', auth.LoginView.as_view(template_name= 'login.html'), name = 'login'),
    path('logout/', auth.logout_then_login, name= 'logout'),

    path("", views.Inicio.as_view(), name='inicio'),
    #OBJETIVOS
    path('objetivos/', views.objetivos, name='objetivos'),
    path('informacion/', views.informacion, name='informacion'),
    path('contexto/', views.contexto, name='contexto'),

    # Includes

    path('usuarios/', include('apps.usuarios.urls')),
    path('posts/', include('apps.posts.urls')),
]
