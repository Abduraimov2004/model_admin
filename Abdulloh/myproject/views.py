from .models import Category, Product, Comment
from django.shortcuts import render



def index(request):
    return render(request, 'index.html')


def waiting(request):
    return render(request, 'waiting.html')
