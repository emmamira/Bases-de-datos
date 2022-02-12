from django.shortcuts import render

# Create your views here.

def Curso(self):

    curso= Curso(nombre="Desarrollo web", camada="19881")
    curso.save()
    documentoDeTexto=f"--->Curso: {curso.nombre} Camada: {curso.camada}"

    return HttpResponse(documentoDeTexto)