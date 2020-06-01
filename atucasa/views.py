# Create your views here.
from django.shortcuts import render, get_object_or_404, render_to_response
from rest_framework import generics
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView 
from Api.models import Ciudad, Tipo
# from Api.serializers import *

class HomeView(ListView):    
    context_object_name = 'home'  
    model = Ciudad #las vistas basadas en clase solo traen 1 modelo por defecto
    template_name = 'api/index.html'

    #Asi que modificamos el metodo que trae los modelos get_contex_data agregando el nuevo contexto
    # mas info: http://django-book.blogspot.com/2012/11/vistas-genericas-basadas-en-clase.html
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['type'] = Tipo.objects.all()
        return context            

def registration(request):
   return render(request, 'registration/registration_form.html')

# class aa(ListView):
#     model = Ciudad
#     template_name = 'api/index.html'
   
# class CiudadList(generics.ListCreateAPIView):  #get post
#     queryset = Ciudad.objects.all()
#     serializer_class = CiudadSerializer

# class CiudadDetail(generics.RetrieveDestroyAPIView):  #detele, put
#     queryset = Ciudad.objects.all()
#     serializer_class = CiudadSerializer

# class TipoList(generics.ListCreateAPIView):  #get post
#     queryset = Tipo.objects.all()
#     serializer_class = TipoSerializer

# class EmpresasList(generics.ListCreateAPIView):  #get post
#     queryset = Empresas.objects.all()
#     serializer_class = EmpresasSerializer

# class ViewHome(generic.DetailView):
#     # queryset = Ciudad
#     template_name = 'consultas/home/'
