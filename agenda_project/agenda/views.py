from django.shortcuts import render, redirect
from .models import Contacto

def home(request):
    contactoListado = Contacto.objects.all()
    return render(request, "gestionContacto.html", {"contacto": contactoListado})

def registrarContacto(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    telefono = request.POST['numTelefono']
    email = request.POST['txtEmail']

    contacto = Contacto.objects.create(codigo = codigo, nombre = nombre, apellido = apellido, telefono = telefono, email = email,)
    return redirect('/')

def edicionContacto(request,codigo):
    contacto = Contacto.objects.get(codigo = codigo)
    return render(request,"edicionContacto.html", {"contacto" : contacto})

def editarContacto(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    telefono = request.POST['numTelefono']
    email = request.POST['txtEmail']

    contacto = Contacto.objects.get(codigo = codigo)
    contacto.nombre = nombre
    contacto.apellido = apellido
    contacto.telefono = telefono
    contacto.email = email
    contacto.save()
    return redirect('/')


def eliminarContacto(request, codigo):
    contacto = Contacto.objects.get(codigo = codigo)
    contacto.delete()
    return redirect('/')
