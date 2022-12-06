from django.shortcuts import render
from .models import Products, Employees, Inventory
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test

def not_in_estoquista_group(user):
    if user:
        return user.groups.filter(name='Estoquista').count() == 0
    return False

# Create your views here.
@login_required
def list_products(request):
    print(request.user.first_name)
    e = get_object_or_404(Employees, id_e= request.user.username)
    p= Products.objects.all()
    i= Inventory.objects.all()
    context= {'products_list': p, 'employee': e, 'inventory_list': i}
    return render(request, 'warehouse/index.html', context)

@login_required
def create_product(request):
    e = get_object_or_404(Employees, id_e= request.user.username)
    if request.method == 'POST':
        product_name = request.POST['name']
        product_code= request.POST['bar_code']
        product_qtt = request.POST['qtt']
        product_img= request.FILES['img']
        fss = FileSystemStorage()
        file = fss.save(product_img.name, product_img)
        file_url = fss.url(file)
        p = Products(name=product_name, bar_code= product_code, qtt=product_qtt, img= file_url)
        p.save()
        i= Inventory(product= p, employee= e, qtt= product_qtt, mov= 'E')
        i.save()
        return HttpResponseRedirect(reverse('warehouse:index'))
    else:
        context= {'employee': e}
        return render(request, 'warehouse/cad_prod.html', context)

#New Products Supply
@login_required
def update_product(request):
    e = get_object_or_404(Employees, id_e= request.user.username)
    if request.method == 'POST':
        product_code= request.POST['bar_code']
        product_qtt = request.POST['qtt']
        p = get_object_or_404(Products, bar_code= product_code)
        p.bar_code= product_code
        p.qtt= p.qtt + int(product_qtt)
        p.save()
        i= Inventory(product= p, employee= e, qtt= product_qtt, mov= 'E')
        i.save()
        return HttpResponseRedirect(reverse('warehouse:index'))
    else:
        context= {'employee': e}
        return render(request, 'warehouse/entrada.html', context)

#New Product Order
@login_required
def update_product2(request):
    e = get_object_or_404(Employees, id_e= request.user.username)
    if request.method == 'POST':
        product_code= request.POST['bar_code']
        product_qtt = request.POST['qtt']
        p = get_object_or_404(Products, bar_code= product_code)
        p.qtt= p.qtt - int(product_qtt)
        p.save()
        i= Inventory(product= p, employee= e, qtt= product_qtt, mov= 'S')
        i.save()
        return HttpResponseRedirect(reverse('warehouse:index'))
    else:
        context= {'employee': e}
        return render(request, 'warehouse/saida.html', context)

@login_required
@user_passes_test(not_in_estoquista_group, login_url='warehouse:index')
def create_employee(request):
    e2 = get_object_or_404(Employees, id_e= request.user.username)
    if request.method == 'POST':
        employee_name = request.POST['name']
        employee_id= request.POST['id_e']
        employee_position = request.POST['position']
        employee_password = request.POST['password']
        employee_img= request.FILES['img_e']
        print("\n\nValor do radio é: " + employee_position + "\n\n")
        if employee_position == '1':
            employee_position= " "
            employee_position= "Estoquista"
        if employee_position == '2':
            employee_position= " "
            employee_position= "Gestor de estoque"
        fss = FileSystemStorage()
        file = fss.save(employee_img.name, employee_img)
        file_url = fss.url(file)
        user= User.objects.filter(username= employee_id).first()
        if user:
            return HttpResponseRedirect(reverse('warehouse:cad_func'))
        else:
            user= User.objects.create_user(username= employee_id, first_name= employee_name, password= employee_password)
            user.save()
            user_group= Group.objects.get(name= employee_position)
            user.groups.add(user_group)
            e = Employees(id_e= employee_id, name= employee_name, position= employee_position, password= employee_password, img_e= file_url)
            e.save()
            return HttpResponseRedirect(reverse('warehouse:index'))
    else:
        context= {'employee': e2}
        return render(request, 'warehouse/cad_func.html', context)

@login_required
def history(request, bar_code):
    e = get_object_or_404(Employees, id_e= request.user.username)
    p = get_object_or_404(Products, bar_code= bar_code)
    i = Inventory.objects.filter(product= p.id)
    #print("\n\n", i[2].mov, "\n\n")
    context= {'employee': e, 'inventory_list': i}
    return render(request, 'warehouse/historico.html', context)

'''
def search_products(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        products_list = product.objects.filter(name__icontains=search_term)
        context = {"products_list": products_list}
    return render(request, 'products/search.html', context)
'''