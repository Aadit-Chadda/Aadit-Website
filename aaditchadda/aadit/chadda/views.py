from django.shortcuts import render
from django.http import HttpResponse


def news(request):
    return render(request, 'chadda/landing.html')

def blogs(request):
    return render(request, 'chadda/blogs.html')

