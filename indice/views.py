from django.http import HttpResponse
import random
from django.shortcuts import render


from django.template import loader


def inicio(request):
    return render(request, "indice/index.html", {})

def otra_vista(request):
    return HttpResponse('''
                        <h1>Este es un titulo en h1</h1>
                        ''')

def numero_random(request):
    numero = random.randrange(15, 180)
    texto = f'<h1>Este es tu numero random: {numero}</h1>'
    return HttpResponse(texto)

def nombre_del_usuario(request, numero):
    texto = f'<h1>Este es tu numero: {numero}</h1>'
    return HttpResponse(texto)

def mi_plantilla(request):

    nombre = 'Jorgeliina'
    apellido = 'Atahualpa'

    lista = [3, 1, 2, 45, 1, 2, 3]

    diccionario_de_datos = {
        'nombre': nombre,
        'apellido': apellido,
        'nombre_largo': len(nombre),
        'lista': lista
    }
    
    #VERSION VIEJA CON open
    #plantilla = open(r"/Users/natalialin/Desktop/miproyecto/miproyecto/plantillas/mi_plantilla.html")
    #template = Template(plantilla.read())
    #plantilla.close()
    #context = Context(diccionario_de_datos)
    #plantilla_preparada = template.render(diccionario_de_datos)


    #VERSION NUEVA CON loader
    #template = loader.get_template("mi_plantilla.html")
    #plantilla_preparada = template.render(diccionario_de_datos)
    #return HttpResponse(plantilla_preparada)

    #VERSION CON render
    return render(request, "indice/mi_plantilla.html", diccionario_de_datos)