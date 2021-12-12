from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

# Create your views here.

from .models import Post
from .forms import *

class Inicio_Posts(ListView):
    template_name = "posts/posts.html"
    model = Post
    context_object_name = "posts"
        
    # return de query + filter
    def get_queryset(self):
        # self.request
        return Post.objects.all().order_by("id")

class AgregarPost(CreateView):
    template_name= "posts/agregar.html"
    model = Post
    form_class = PostForm

    def get_success_url(self, **kwargs) -> str:
        return reverse_lazy("posts:inicio_posts")