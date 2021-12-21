from django import forms
from django.db import models
from django.db.models import fields
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Comentario, Post


class Post_Form(forms.ModelForm):
	titulo = forms.CharField(label='Titulo',
		widget=forms.TextInput(attrs={
			'class': 'col-sm-6'
		})
    )
	cuerpo = forms.CharField(label='Cuerpo',
		widget=forms.TextInput(attrs={
			'class': 'col-sm-6'
		})
    )

	es_borrador = forms.BooleanField(required=False)


	class Meta:
		model = Post
		fields = {'titulo', 'cuerpo', 'es_borrador'}



@login_required
def Editar_Post(request):
	user = request.user.id
	post = Post.objects.get(autor = user)

	if request.method == 'POST':
		form = Post_Form(request.POST, instance= post)
		if form.is_valid():
			post.titulo = form.cleaned_data.get('titulo')
			post.cuerpo = form.cleaned_data.get('cuerpo')
			post.es_borrador = form.cleaned_data.get('es_borrador')

			post.save()

			return redirect('posts:mis_posts')
	else:
		form = Post_Form(instance=post)

	context = {
		'form': form
	}
	return render('posts/edit.html')




# class Post_Form(forms.ModelForm):
#     """Form definition for MODELNAME."""

#     class Meta:
#         """Meta definition for MODELNAMEform."""
#         model = Post
#         fields = ('titulo',
#                 'cuerpo',
#                 'es_borrador',
#                 )
#         labels = {
#                 'titulo': 'Título',
#                 'cuerpo':'Escribe aquí',
#                 'es_borrador':'Borrador',
#         }

class Comment_Post(forms.ModelForm):
	cuerpo = forms.CharField(
		widget=forms.TextInput(attrs={
			'class': 'col-sm-6'
		})
    )

	class Meta:
		model = Comentario
		fields = {'cuerpo'}