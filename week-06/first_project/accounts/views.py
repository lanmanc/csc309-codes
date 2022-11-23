from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, HttpResponseNotFound
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import FormView, RedirectView

from accounts.forms import SignupForm, LoginForm


def hello(request, name):
    print(request.GET)
    return HttpResponse(f"hey {name} there! **** Logged-in user: {request.user.username}")


def signup(request):
    if request.method == "GET":
        return TemplateResponse(request, 'accounts/signup.html')
    elif request.method == "POST":
        print(request.POST)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        errors = []
        if password != password2:
            errors += ["Passwords do NOT match"]
        if len(username) < 4:
            errors += ["Username must be at least 4 characters"]

        if errors:
            return TemplateResponse(request, 'accounts/signup.html', {'errors': errors})

        # Create a user
        User.objects.create_user(username=username, password=password)
        return HttpResponseRedirect(f"/accounts/hello/{username}")
    else:
        return HttpResponseNotFound()


class SignupView(View):
    def get(self, request):
        print(self)
        return TemplateResponse(request, 'accounts/signup.html')

    def post(self, request):
        print(self)
        print(request.POST)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        errors = []
        if password != password2:
            errors += ["Passwords do NOT match"]
        if len(username) < 4:
            errors += ["Username must be at least 4 characters"]

        if errors:
            return TemplateResponse(request, 'accounts/signup.html', {'errors': errors})

        # Create a user
        User.objects.create_user(username=username, password=password)
        return HttpResponseRedirect(f"/accounts/hello/{username}")


class SignupFormView(FormView):
    template_name = 'accounts/form.html'
    form_class = SignupForm

    def form_valid(self, form):
        User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'])
        return HttpResponseRedirect(f"/accounts/hello/{form.cleaned_data['username']}")


class LoginView(FormView):
    template_name = 'accounts/form.html'
    form_class = LoginForm

    def form_valid(self, form):
        login(self.request, form.cleaned_data['user'])
        return HttpResponseRedirect(f"/accounts/hello/{form.cleaned_data['user'].username}")


class RedirectToHome(RedirectView):
    pattern_name = '/accounts/home/'

