from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect

def stone(request):
    content = {}
    return render(request, "stone/index.html", content)