from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
def home(request):
    html ="<html><body><h1>Home Page</h1></body></html>"
    return HttpResponse(html)


class register(View):
    def get(self,request):
        return render(request, 'register.html')

class login(View):
    def get(self,request):
        return render(request, 'login.html')

def about(request):
    html ="<html><body><h1>About</h1></body></html>"
    return HttpResponse(html)


def index(request):
    html ="<html><body><h1>This in index page</h1></body></html>"
    return HttpResponse(html)


def test(request):
    html ="<html><body><h1>This is test page</h1></body></html>"
    return HttpResponse(html)


def contact(request):
    html ="<html><body><h1>Contact Form</h1></body></html>"
    return HttpResponse(html)




    


