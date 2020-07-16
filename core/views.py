from django.shortcuts import render, redirect, HttpResponse
from core.models import Evento
import os
import sys

#
# def index(request):
#     return redirect('/agenda/')


# Create your views here.
def eventos(request, titulo_evento):
    local = Evento.objects.get(titulo=titulo_evento)

    return HttpResponse('O local do evento será: {}'.format(local))


def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
