from django.shortcuts import render,redirect
from .services import *
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def libro(request):
    if request.method == 'POST':
        form = CrearLibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro guardado correctamente')
            return redirect('libro')
        else:
            messages.error(request, 'Error al guardar el libro')
    else:
        
        form = CrearLibroForm()
        context = {'form':form}
    return render(request, 'libro/index.html', context)

def listar(request):
    libros = listar_libros()
    context = {'libros':libros}
    return render(request, 'libro/listar.html', context)

