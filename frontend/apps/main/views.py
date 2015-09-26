from django.shortcuts import render, redirect
from django.http import HttpResponse

# Homepage View
def show_homepage(request):
    context = {}

    return render(request, 'main.html', context)