from django.shortcuts import render

from apps.usuarios.models import Usuario
from apps.posts.models import Post
from django.views.generic.base import TemplateView
from django.views.generic import  ListView

# vista basada en funcion

def objetivos(request):
    return render(request, 'objetivos.html')

    
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



#     template_name= "index.html"

#     def get_context_data(self, **kwargs):
#         context = super(Inicio, self).get_context_data(**kwargs)
#         context["informacion"] = "--> views.py (class 'Inicio')  --> get_context_data()"
#         return context
