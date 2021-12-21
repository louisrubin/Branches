from django.shortcuts import render

from apps.usuarios.models import Usuario
from apps.posts.models import Post
from django.views.generic import  ListView
from apps.posts.models import Comentario
from apps.posts.forms import Comment_Post

# vista basada en funcion

def objetivos(request):
    return render(request, 'objetivos.html')

def informacion(request):
    return render(request, 'informacion.html')

def contexto(request):
    return render(request, 'contexto.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    pass

# vista basada en clases

class Inicio(ListView):

    template_name = "index.html"
    model = Post
    context_object_name = "posts"   

  
    def get_queryset(self):
        if self.request.user:
            return Post.objects.all()