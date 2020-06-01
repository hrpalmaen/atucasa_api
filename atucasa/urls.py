from django.conf.urls import url, include
from Api.views import HomeView 
from django.views.generic import TemplateView


urlpatterns = [
    #agrego el contexto en la url (por que aun no se jeje)
    url('', HomeView.as_view(context_object_name="type"), name='index'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),



     #url(r'^accounts/registration/', views.registration, name='registration'),


    # url('home/', TemplateView.as_view(template_name='home.html')),
    #  url('ciudad/', views.CiudadList.as_view()),
    # # path('ciudad/', views.CitiesList.as_view()),
    # url('usuario/<int:pk>/', views.CiudadDetail.as_view()),    
    # # path('empresa/<int:pk>/', views.BusinessDetail.as_view())
    # url('tipo/', views.TipoList.as_view()),
    # url('empresas/', views.EmpresasList.as_view()),
    
    # url('vista2/', TemplateView.as_view(template_name='prueba.html'))

]