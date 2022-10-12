from django.shortcuts import render

def add(request):
    data = request.POST.get('result')
    