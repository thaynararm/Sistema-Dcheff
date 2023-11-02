from django.shortcuts import render

def index(request):
    return render(request, 'index/index2.html')