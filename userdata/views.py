from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserProfileForm
from django.views.generic.edit import FormView
# Create your views here.


def profile(request):
    userprofile = request.user.profile
    if request.method == "POST":
        # userprofile = request.user.profile
        form = UserProfileForm(request.POST, instance=userprofile)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(
                request, "Succesfully updated shipping information.")
        else:
            messages.error(request, "Something went wrong. Try again.")
    form = UserProfileForm(instance=userprofile)
    return render(request, "userdata/profile.html", {
        "form": form
    })

# class ProfileView(FormView):
#     template_name = 'profile.html'
#     form_class = UserProfileForm
#     success_url = 'profile.html'


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("homepage")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, "userdata/register.html", {
        "register_form": form
    })


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Welcome, {username.capitalize()} !")
                return redirect("homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "userdata/login.html", {
        "login_form": form
    })


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("homepage")
