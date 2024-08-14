from django.shortcuts import render, redirect
from libro.services import *
from libro.forms import *
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    return render(request, 'index.html')
    
def editar(request, id):
    libro = buscar_libro(id)
    return HttpResponse(libro)

    