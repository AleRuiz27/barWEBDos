from django.shortcuts import render
from django.http import HttpResponse
from .models import conciertos,Person
from django.db import connection
# Create your views here.
def base(request):
    return render(request, 'index.html')


def RESULT(request):
    return render(request, 'def.html')


def formt(request):
    return render(request, 'formularioDeCarga.html')



def ver_eventos(request):
    with connection.cursor() as recorrer:
        recorrer.execute('select * from conciertos')
        row = recorrer.fetchall()
        c = conciertos.objects.all()

    return HttpResponse(row)






#def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'def.html',{'eventos': eventos})
