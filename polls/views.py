import math
from django.http import HttpResponse
from django.template import loader

import pdb
from HashIndexExample.src.classes.DatabaseForm import DatabaseForm
from HashIndexExample.src.classes.Parameters import Parametros
from polls.controller import Controller


controller = Controller()
context = {
        'params': Parametros(),
       
    }
def index(request):
    template = loader.get_template('polls/index.html')
    form = DatabaseForm()
    if request.method == 'POST':
        form = DatabaseForm(request.POST, request.FILES)
        context['form'] = form
        
        if form.is_valid():
            file = request.FILES.get('file', None)
            
            params = Parametros()

            params.tamanho_bucket = form.cleaned_data['tamanho_bucket']
            params.tamanho_pagina = form.cleaned_data['tamanho_pagina']
            params.total_buckets = form.cleaned_data['total_buckets']
            
            context['params'] = params
            lines = file.readlines()

            quant_min_bucket = math.ceil(len(lines) / params.tamanho_bucket)

            if params.total_buckets <= quant_min_bucket:
                context['errorMessage'] = "a quant. de buckets deve ser maior que: " + str(quant_min_bucket)
                return HttpResponse(template.render(context, request))


            bancoDeDados = controller.load_file(lines, params)
            context['bancoDeDados'] = bancoDeDados 

            Response = HttpResponse(template.render(context, request))
            
            Response.set_cookie('bancoDeDados',bancoDeDados)
            Response.set_cookie('params', Parametros())
            Response.set_cookie('form', form)
            
            return Response

    else:
        context['form'] = form
        return HttpResponse(template.render(context, request))



def search_tuple(request):
    context['palavra'] = ''
    template = loader.get_template('polls/index.html')
    if request.GET.get('key_search'):
        palavra = request.GET.get('key_search')
        
        context['palavra'] = controller.buscar(palavra)
        
    return HttpResponse(template.render(context, request))


def table_scan(request):
    context['items']=None
    if request.GET.get('table_scan'):
        template = loader.get_template('polls/index.html')
        quantidade = request.GET.get('table_scan')
        context['items'] = controller.mostrar_registros(int(quantidade))

        
    return HttpResponse(template.render(context, request))

