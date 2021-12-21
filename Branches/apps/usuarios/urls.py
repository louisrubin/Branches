from django.urls import path

from . import views

app_name = "usuarios"

urlpatterns = [
    path('', views.usuarios, name='usuarios'),
    path("registro/", views.RegistroUsuario.as_view(), name="registro"),
    path("perfil/", views.PerfilUsuario.as_view(), name="perfil"),
    path("editar/<int:pk>/", views.Editar_Own_Perfil.as_view(), name="editar_perfil"),

    # ADMIN
    path("admin/listar/", views.ListarAdmin.as_view(), name="admin_listar"),
    path("admin/ver-perfil/<int:pk>/", views.Ver_Perfil_Admin.as_view(), name="admin_ver_perfil"),
    path("admin/editar/<int:pk>/", views.Editar_only_Admin.as_view(), name= "admin_editar"),
    path("admin/delete/<int:pk>/", views.Delete_User.as_view(), name="delete_user"),
]
