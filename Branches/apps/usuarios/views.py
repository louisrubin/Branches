from django.contrib.auth.mixins import LoginRequiredMixin
from django.db                  import models
from django.shortcuts           import render
from django.urls                import reverse_lazy
from django.views.generic       import ListView, CreateView
from django.views.generic.edit  import DeleteView, UpdateView, DeleteView
from  apps.core.mixins import AdminRequiredMixins

# Create your views here.
from .forms import UsuarioForm, RegistroForm
from .models import Usuario

def usuarios(request):
    return render(request, 'usuarios/usuarios.html')

class ListarAdmin(LoginRequiredMixin, AdminRequiredMixins, ListView):
    template_name = "usuarios/admin/listar.html"
    model = Usuario
    context_object_name = "usuarios"
        
    # return de query + filter
    def get_queryset(self):
        # self.request
        return Usuario.objects.all().order_by("id")
    
"""
class Nuevo_only_Admin(CreateView):
    template_name= "usuarios/admin/nuevo.html"
    model = Usuario
    form_class = UsuarioForm

    def get_success_url(self, **kwargs) -> str:
        return reverse_lazy("usuarios:admin_listar")
"""


class Editar_only_Admin(UpdateView):
    template_name= "usuarios/admin/editar.html"
    model = Usuario
    form_class = UsuarioForm

    success_url = reverse_lazy("usuarios:admin_listar")



class RegistroUsuario(CreateView):
    template_name = "usuarios/registro.html"
    model = Usuario
    form_class = RegistroForm

    success_url = reverse_lazy("login")


class PerfilUsuario(ListView):
    template_name = "usuarios/perfil.html"
    model = Usuario
    form_class = UsuarioForm

    context_object_name = "usuario_data"


class Delete_User(DeleteView):
    template_name = "usuarios/admin/delete_user.html"
    model = Usuario

    success_url = reverse_lazy("usuarios:admin_listar")
