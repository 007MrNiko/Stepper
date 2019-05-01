from django.shortcuts import render, redirect

from django.http import HttpResponse

#connecting of html file (section "about")
def index(request):
    return render(request, 'index_about.html')
