from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request handler
def index(request):
    return render(request, "playground/hello.html")
def say_hello(request):
    return render(request, 'hello.html', {'name': 'mosh'})
def brian(request):
    return HttpResponse("Hello, brian")
def david(request):
    return HttpResponse("hello, david")
def greet(request, name):
    return HttpResponse(f"hello, {name.capitalize()}")
