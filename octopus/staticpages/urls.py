from django.urls import path
from . import views

urlpatterns = [
    path('cad_func/', views.cad_func, name='cad_func'),
    path('cad_prod/', views.cad_prod, name='cad_prod'),
    path('entrada/', views.entrada, name='entrada'),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('saida/', views.saida, name='saida'),
]