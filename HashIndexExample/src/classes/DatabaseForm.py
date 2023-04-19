from django import forms

class DatabaseForm(forms.Form):
    file = forms.FileField(label='Arquivo',required=True)
    tamanho_pagina = forms.IntegerField(label= 'Quant. de registros por página', required=True)
    total_buckets = forms.IntegerField(label = 'total de buckets', required=True)
    tamanho_bucket = forms.IntegerField(label = 'Quant. de registros por bucket', required=True)