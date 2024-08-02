from django.shortcuts import render
from django.http import HttpResponse

# Создайте здесь свои представления.
def index(request):
    return render(request, "main/index.html")

def data(request):
    return render(request, "main/data.html")

def test(request):
    return render(request, "main/test.html")
