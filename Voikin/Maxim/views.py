from django.shortcuts import render
from django.http import HttpResponse

def empty(request):
    return render(request, 'empty.html')

def name(request):
    return render(request, 'name.html')

def groupe(request):
    return render(request, 'groupe.html')

def age(request):
    return render(request, 'age.html')

def common(request):
    return render(request, 'common.html')

