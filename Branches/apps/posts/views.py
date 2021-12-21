from django.http import request
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.base import View
from django.views.generic.edit import DeleteView, UpdateView
from apps.core.mixins import WriterRequiredMixins, CommentRequiredMixins


# Create your views here.

from .models import Post, Comentario
from .forms import *



class Mis_Posts(LoginRequiredMixin, ListView):

    template_name = "posts/my_posts.html"
    model = Post
    context_object_name = "posts"   
    paginate_by = 4
    
    def get_queryset(self):
        return Post.objects.filter(autor = self.request.user.id).order_by("id")


class Agregar_Post(LoginRequiredMixin, WriterRequiredMixins, CreateView):
    template_name= "posts/new_post.html"
    model = Post

    form_class = Post_Form

    # agrega el id del user al campo foreingkey automaticamente
    def form_valid(self, form):
        f = form.save(commit= False)
        f.autor_id = self.request.user.id
        return super(Agregar_Post, self).form_valid(form)

    success_url = reverse_lazy("posts:mis_posts")


class Ver_Post(LoginRequiredMixin, View):
      
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk = pk)

        form = Comment_Post()

        comentarios = Comentario.objects.filter(post = post).order_by('-fecha_creacion')

        context = {
            'post': post,
            'form': form,
            'comentarios': comentarios,
        }
        return render(request, 'posts/ver_post.html', context) 




    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk = pk)

        form = Comment_Post(request.POST)

        comentarios = Comentario.objects.filter(post = post).order_by('-fecha_creacion')

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.autor = request.user
            new_comment.post = post
            new_comment.save()

        context = {
            'post': post,
            'form': form,
            'comentarios': comentarios,
        }
        return render(request, 'posts/ver_post.html', context)

class Editar_Post(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['titulo','cuerpo', 'es_borrador']
    template_name = 'posts/edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk'] # 'pk'                  'pk'
        return reverse_lazy('posts:ver_post', kwargs={'pk': pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor

class Delete_Post(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('posts:mis_posts')

    def test_func(self):
        # 
        post = self.get_object()
        return self.request.user == post.autor

