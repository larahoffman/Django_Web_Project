from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("Holis")

def probandoTemplate(self):

    nombre = "Pepe"
    apellido = "Etesech"
    notas = [1,2,3,4,5]
    diccionario = {"nombre":nombre, "apellido": apellido, "notas": notas}
    plantilla = loader.get_template('template1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
