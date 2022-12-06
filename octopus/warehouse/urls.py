from django.urls import path

from . import views

app_name = 'warehouse'
urlpatterns = [
    path('', views.list_products, name='index'),
    path('cad_prod/', views.create_product, name='cad_prod'),
    path('cad_func/', views.create_employee, name='cad_func'),
    path('entrada/', views.update_product, name="entrada"),
    path('saida/', views.update_product2, name="saida"),
    path('historico/<int:bar_code>/', views.history, name='history')
]