from django.shortcuts import render
from django.http import HttpResponse
from .models import conciertos,Person
from django.db import connection
# Create your views here.
def base(request):
    return render(request, 'index.html')


def RESULT(request):
    return render(request, 'def.html')

def finish(request):
    return render(request, 'exito.html')

def formt(request):
    return render(request, 'formularioDeCarga.html')

#def post_new(request):
    form = conciertos()
    return render(request, 'formularioDeCarga.html', {'carga': form})

def post_nuevo(request):
        user_name = request.GET.get('user_name')
        user_lugar = request.GET.get('user_lugar')
        trip_start = request.GET.get('trip-start')
    
        
    # if this is a POST request we need to process the form data
    #if request.method == "GET":
        # create a form instance and populate it with data from the request:
    
        with connection.cursor() as insertar:
            insertar.execute(f"INSERT INTO `conciertos` (`ARTISTAS`, `LUGAR`, `FECHA`) VALUES ('{user_name}', '{user_lugar}', '{trip_start}')")
        
        
        return render(request, 'exito.html')

    # if a GET (or any other method) we'll create a blank form
    





def ver_eventos(request):
    with connection.cursor() as recorrer:
        recorrer.execute('select * from conciertos')
        row = recorrer.fetchall()
        c = conciertos.objects.all()

    return HttpResponse(row)






#def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'def.html',{'eventos': eventos})
