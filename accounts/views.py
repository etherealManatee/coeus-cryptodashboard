from accounts.forms import RegisterUserForm
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def register_view(request):
    register = RegisterUserForm()
    if request.method == "POST":
        user = register.save()
        login(request, user)
    
    context = {"register_form" : register}

    return render(request, "accounts/register.html", context)

def login_view(request):
    pass

def logout_view(request):
    pass