from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.models import User


menu = {
    'Login page': '/login',
    'Logout page': '/logout',
    'Sign up page': '/signup',
    'Vacancy list': '/vacancies',
    'Resume list': '/resumes',
    'Personal profile': '/home'
}


# Create your views here.
class MainMenu(View):
    def get(self, request, *args, **kwargs):
        context = {'menu': menu}
        return render(request, 'hyperjob/menu.html', context=context)


class SingUpForm(CreateView):
    form_class = UserCreationForm
    success_url = "login"
    template_name = "registration/signup.html"


class LoginFrom(LoginView):
    redirect_authenticated_user = True
    template_name = 'login/login.html'


class HomeView(View):
    def get(self, request, *args, **kwargs):
        # Default value when user is not authenticated
        manager = None

        # Check if user authenticated
        if request.user.is_authenticated:
            if User().is_staff:
                manager = True
            else:
                manager = False

        context = {'manager': manager}
        return render(request, 'home/home.html', context=context)
