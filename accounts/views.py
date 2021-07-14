from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import RegisterUserForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def register_view(request):
    register = RegisterUserForm()
    if request.method == "POST":
        register = RegisterUserForm(request.POST)
        if register.is_valid():
            user = register.save()
            login(request, user)
            return redirect("dashboard:dashboard_view_page")
    
    context = {"register_form" : register}

    return render(request, "accounts/register.html", context)

def login_view(request):
    login_form = AuthenticationForm()
    
    if request.method == "POST":
        login_form = AuthenticationForm(request.POST)
        if request.method == "POST":
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']

                user = authenticate(username = username, password = password)
                
                if user is not None:
                    login(request, user)
                    return redirect("dashboard:dashboard_view_page")

    context = {"login_form" : login_form}
    return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("accounts:login_view")