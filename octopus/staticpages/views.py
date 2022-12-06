from django.shortcuts import render

# Create your views here.

def cad_func(request):
    context= {}
    return render(request, 'staticpages/cad_func.html', context)

def cad_prod(request):
    context= {}
    return render(request, 'staticpages/cad_prod.html', context)

def entrada(request):
    context= {}
    return render(request, 'staticpages/entrada.html', context)

def index(request):
    context= {}
    return render(request, 'staticpages/index.html', context)

def login(request):
    context= {}
    return render(request, 'staticpages/login.html', context)

def saida(request):
    context= {}
    return render(request, 'staticpages/saida.html', context)