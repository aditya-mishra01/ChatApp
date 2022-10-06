from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def ChatgPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
         return redirect("login-user")
    context = {}
    return render(request, "chat/ChatgPage.html", context)

def ChatooPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat/chatooPage.html", context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('/')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'chat/RegPage.html', context)