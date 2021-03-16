from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def home(request):
    html="<html><body><h1>Hello World</h1></body></html>"
    return HttpResponse(html)

def about(request):
    html="<html><body><h2>This my first page about home</h1></body></html>"
    return HttpResponse(html)

def login(request):
    html="<html><body><h3>Login Form</h3></body></html>"
    return HttpResponse(html)

def register(request):
    html="<html><body><h4>Register Form</h4></body></html>"
    return HttpResponse(html)


    


