from django.urls import path
from . views import *

urlpatterns = [
    path('', view=libro, name='libro'),
    path('listar/', view=listar, name='listar'),
]