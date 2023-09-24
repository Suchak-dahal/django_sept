from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello</h1>")

def root(request):
    people = [
        {"first": "John", "last": "Doe", "address": "KTm"},
        {"first": "Jane", "last": "Dae", "address": "Bktm"},
        {"first": "Ram", "last": "Doaae", "address": "hKTm"},
        {"first": "shyam", "last": "Dawoe", "address": "KjjTm"},
    ]
    student = {"name": "John", "age": "12", "address": "ktm"}
    return render(request, template_name = "myapp/root.html", context ={"title": "Root Page", "people": people})
