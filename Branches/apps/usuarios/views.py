from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView

# Create your views here.
from .forms import ProductoForm, RegistroForm
from .models import Usuario

def usuarios(request):
    return render(request, 'usuarios/usuarios.html')

class ListarAdmin(ListView):
    template_name = "usuarios/admin/listar.html"
    model = Usuario
    context_object_name = "usuarios"
        
    # return de query + filter
    def get_queryset(self):
        # self.request
        return Usuario.objects.all().order_by("id")
    

class Nuevo_only_Admin(CreateView):
    template_name= "usuarios/admin/nuevo.html"
    model = Usuario
    form_class = ProductoForm

    def get_success_url(self, **kwargs) -> str:
        return reverse_lazy("usuarios:admin_listar")



class Editar_only_Admin(UpdateView):
    template_name= "usuarios/admin/editar.html"
    model = Usuario
    form_class = ProductoForm

    def get_success_url(self, **kwargs) -> str:
        return reverse_lazy("usuarios:admin_listar")



class RegistroUsuario(CreateView):
    template_name = "usuarios/registro.html"
    model = Usuario
    form_class = RegistroForm

    success_url = reverse_lazy("login")