from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib import messages

def login_user(request):
    if request.method == "POST":
        print("CCCCCCCC")
        id_e= request.POST['id_e']
        password= request.POST['password']
        user= authenticate(request, username= id_e, password= password)
        if user is not None:
            print("AAAAAAA")
            login_django(request, user)
            return HttpResponseRedirect(reverse('warehouse:index'))
        else:
            print("BBBBBBB")
            messages.success(request, ("Houve um erro ao entrar na conta Octopus. Tente novamente..."))
            return  redirect('login')
    else:
        return render(request, 'registration/login.html', {})

def logout(request):
    logout_django(request)
    return render(request, 'registration/login.html', {})

'''
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
'''