from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.


def logoutpage(request):
    logout(request)
    return render(request, "authenticate/logout.html")


def loginpage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("Home")
            else:
                print("Invalid username or password")
        else:
            print("Invalid username or password")
    form = AuthenticationForm()
    return render(request, "authenticate/login.html", context={"login_form": form})


def registerpage(request):
    return render(request, "authenticate/register.html")
