from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
from AppFamiliar.models import Familia

def lista_familiar(request):

    data_familia = Familia.objects.all()

    template = loader.get_template(r'C:\Users\pc1\OneDrive\Escritorio\MVT_Santiago_Ribecca\MVT_Santiago\MVT_Santiago\templates\index.html')

    data = {'Familia': data_familia}

    documento = template.render(data)

    return HttpResponse(documento)

    #context = {'lista': 'Base de Datos Familia'}
    #return render(request, 'index.html', context)


