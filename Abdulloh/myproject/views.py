from django.shortcuts import render


def car(request):
    return render(request, 'car.html')


def waiting(request):
    return render(request, 'waiting.html')