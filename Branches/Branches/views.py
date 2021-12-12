from django.shortcuts import render

from apps.usuarios.models import Usuario
from django.views.generic.base import TemplateView

# vista basada en funcion
"""
def inicio(request):

    context = {
        "usuarios": Usuario.objects.all(),  # genera una query del tipo 'SELECT * ' con .all()   ||||   # usuario1 = Usuario.objects.get(id=1)
    }
    return render(request, 'index.html', context)
"""
def login(request):
    return render(request, 'login.html')

def logout(request):
    pass

# vista basada en clases

class Inicio(TemplateView):
    template_name= "index.html"

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context["informacion"] = "--> views.py (class 'Inicio')  --> get_context_data()"
        return context
