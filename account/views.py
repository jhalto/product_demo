from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout


# Create your views here.
def register(request):
    
    if request.method == "POST":
        print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    
    context = {
        'form': form
    }
    return render(request, 'register_view.html' , context)

def login(request):
    
    if request.method == "POST":
        print(request.POST)
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            print(form)
            user = form.get_user()
            print(user)
            user_login(request, user)
            return redirect('home_view')
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form
    }
    return render(request, 'login_view.html' , context)


def logout(request):
    user_logout(request)
    return redirect('login')