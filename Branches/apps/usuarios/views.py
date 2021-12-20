from django.contrib.auth.mixins import LoginRequiredMixin
from django.db                  import models
from django.shortcuts           import render
from django.urls                import reverse_lazy
from django.views.generic.base  import View
from django.views.generic       import ListView, CreateView
from django.views.generic.edit  import DeleteView, UpdateView, DeleteView
from  apps.core.mixins import AdminRequiredMixins

# Create your views here.
from .forms import UsuarioForm, RegistroForm
from .models import Usuario

def usuarios(request):
    return render(request, 'usuarios/usuarios.html')


class PerfilUsuario(LoginRequiredMixin, ListView):
    template_name = "usuarios/perfil.html"
    model = Usuario
    form_class = UsuarioForm

    context_object_name = "usuario_data"


class ListarAdmin(LoginRequiredMixin, AdminRequiredMixins, ListView):
    template_name = "usuarios/admin/listar.html"
    model = Usuario
    context_object_name = "usuarios"
    paginate_by = 10

    def get_queryset(self):
        return Usuario.objects.all().order_by("id")


class Ver_Perfil_Admin(AdminRequiredMixins, View):
    # template_name = "usuarios/admin/admin-ver-perfil.html"    # url: admin_ver_perfil
    # model = Usuario
    # form_class = UsuarioForm
    # context_object_name = "usuario"

    
    def get(self, request, pk, *args, **kwargs):
        perfil = Usuario.objects.get(pk = pk)

        context = {
            'perfil': perfil,
        }
        return render(request, 'usuarios/admin/admin-ver-perfil.html', context) 


    def post(self, request, pk, *args, **kwargs):
        perfil = Usuario.objects.get(pk = pk)

        context = {
            'perfil': perfil,
        }
        return render(request, 'usuarios/admin/admin-ver-perfil.html', context)




class Editar_only_Admin(AdminRequiredMixins, UpdateView):
    template_name= "usuarios/admin/editar.html"
    model = Usuario
    form_class = UsuarioForm

    success_url = reverse_lazy("usuarios:admin_listar")



class RegistroUsuario(CreateView):
    template_name = "usuarios/registro.html"
    model = Usuario
    form_class = RegistroForm

    success_url = reverse_lazy("login")



class Delete_User(AdminRequiredMixins, DeleteView):
    template_name = "usuarios/admin/delete_user.html"
    model = Usuario

    success_url = reverse_lazy("usuarios:admin_listar")
