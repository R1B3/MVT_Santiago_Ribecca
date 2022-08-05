from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
from AppFamiliar.models import Familia

def lista_familiar(request):

    template = loader.get_template('C:/Users/pc1/OneDrive/Escritorio/MVT_Santiago_Ribecca/MVT_Santiago/MVT_Santiago/templates/index.html')
    
    data_familia = Familia.objects.all()

    context = {'Familia': data_familia}
    
    documento = template.render(context)
    
    return HttpResponse(documento)




