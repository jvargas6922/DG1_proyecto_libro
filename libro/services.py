from .models import *
from django.utils import timezone as Now

def listar_libros():
    return Libro.objects.all()

def buscar_libro(id):
    try:
        return Libro.objects.get(id_libro=id)
    except Exception as e:
        return e
    
def crear_libro(titulo, autor, fecha_publicacion=None):
    try:
        libro = Libro(
            titulo = titulo,
            autor = autor,
            fecha_publicacion = fecha_publicacion
        )
        libro.save()
        return libro
    except Exception as e:
        return e
    
def actualizar_libro(id, titulo=None, autor=None, fecha_publicacion=None):
    try:
        libro = buscar_libro(id)
        if titulo:
            libro.titulo = titulo
        if autor:
            libro.autor = autor
        if fecha_publicacion:
            libro.fecha_publicacion = fecha_publicacion
        libro.save()
        return libro
    except Exception as e:
        return e
    
def eliminar_libro(id):
    try:
        libro = buscar_libro(id)
        libro.delete()
        return libro
    except Exception as e:
        return e

    
