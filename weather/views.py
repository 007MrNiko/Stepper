from django.shortcuts import render, redirect
from django.http import HttpResponse

#connecting of html file (section "weather")
def index(request):
    return render(request, 'index.html')
