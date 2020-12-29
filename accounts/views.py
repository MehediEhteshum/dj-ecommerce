from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import LoginForm, SignupForm

User = get_user_model()

# Create your views here.


def signup_view(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password1 = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        try:
            user = User.objects.create_user(username, email, password1)
        except:
            user = None
        if user != None:
            # user is valid
            # request.user == user
            login(request, user)
            return redirect("/")
        else:
            # 1 == True
            request.session["signup_error"] = 1
    return render(request, "form.html", {"form": form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user != None:
            # user is valid and active
            # request.user == user
            login(request, user)
            return redirect("/")
        else:
            # attempt = request.session.get("attempt") or 0
            # request.session["attempt"] = attempt + 1
            # return redirect("/invalid-password")
            request.session["invalid_user"] = 1
    return render(request, "form.html", {"form": form})


def logout_view(request):
    # request.user == Anon user
    logout(request)
    return redirect("/login")
