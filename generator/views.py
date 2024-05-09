from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render (request, 'home.html')

def about(request):
    return render (request, 'about.html', )

def contrasena(request):

    caracteres = list('abcdefghijklmnopqrstuvwxyz')
    contrasena_generada = ''

    longitud = int(request.GET.get('longitud'))

    if request.GET.get('mayuscula'):
        caracteres.extend (list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('especiales'):
        caracteres.extend(list('@$#~-_'))

    if request.GET.get('numeros'):
        caracteres.extend(list('1234567890'))

    for x in range(longitud):
        contrasena_generada += random.choice(caracteres)

    return render (request,'contrasena.html', {'contrasena': contrasena_generada})