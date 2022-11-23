from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt


def hello(request, name):
    print(request.GET)
    return HttpResponse(f"hey {name} there!")


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

        return HttpResponseRedirect(f"/accounts/hello/{username}")
    else:
        return HttpResponseNotFound()
