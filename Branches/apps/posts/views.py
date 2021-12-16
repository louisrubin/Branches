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

class Agregar_Post(CreateView):
    template_name= "posts/new_post.html"
    model = Post
    form_class = PostForm

    success_url = reverse_lazy("posts:inicio_posts")
