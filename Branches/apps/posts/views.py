from django.http import request
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.core.mixins import WriterRequiredMixins

from apps.usuarios.models import Usuario

# Create your views here.

from .models import Post
from .forms import *

class Inicio_Posts(LoginRequiredMixin, ListView):

    template_name = "posts/posts.html"
    model = Post
    context_object_name = "posts"   

  
    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.es_administrador:
            return Post.objects.all().order_by("id")
        else:
            return Post.objects.filter(autor = self.request.user.id).order_by("id")


class Mis_Posts(LoginRequiredMixin, ListView):

    template_name = "posts/posts.html"
    model = Post
    context_object_name = "posts"   

    
    # return de query + filter
    def get_queryset(self):
        # self.request
        return Post.objects.filter(autor = self.request.user.id).order_by("id")


class Agregar_Post(WriterRequiredMixins, CreateView):
    template_name= "posts/new_post.html"
    model = Post

    form_class = Post_Form

    # agrega el id del user al campo foreingkey automaticamente
    def form_valid(self, form):
        f = form.save(commit= False)
        f.autor_id = self.request.user.id
        return super(Agregar_Post, self).form_valid(form)

    success_url = reverse_lazy("posts:mis_posts")


