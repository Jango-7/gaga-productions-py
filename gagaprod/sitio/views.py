# from django.shortcuts import render
from django.shortcuts import render
from .models import ProduccionesMod, MultitracksMod, ChartsMod
from sitio.forms import Formulario

# ============= VISTA HOME ================

def home_v(request):
    return render(request, 'index.html')

# ============= VISTA PRODUCCION ==========

def producciones_v(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        telefono = request.POST.get("telefono")
        pedido = request.POST.get("pedido")

        produccion = ProduccionesMod(nombre=nombre, email=email, telefono=telefono, pedido=pedido)
        produccion.save()

        return render(request, 'index.html')

    return render(request, 'producciones.html')

# ============ VISTA MULTITRACKS ==============

def multitracks_v(request):
    if request.method == "POST":
        artista = request.POST.get("artista")
        cancion = request.POST.get("cancion")
        descripcion = request.POST.get("descripcion")

        multitrack = MultitracksMod(artista=artista, cancion=cancion, descripcion=descripcion)
        multitrack.save()

        return render(request, 'index.html')

    return render(request, 'multitracks.html')

# ============ VISTA CHARTS CON API===================

# def charts_v(request):
#     if request.method == "POST":
#         form = Formulario(request.POST)
#         print(f"Es valido:{form.is_valid}")

#         if form.is_valid:
#             datos = form.cleaned_data

#             artista = datos.get("artista")
#             cancion = datos.get("cancion")
#             tonalidad = datos.get("tonalidad")

#             form = Formulario(artista=artista, cancion=cancion, tonalidad=tonalidad)
#             form.save()

#             return render(request, 'index.html')

#     return render(request, 'charts.html')

# ======= VISTA CHARTS ======== 

def charts_v(request):
    if request.method == "POST":
        artista = request.POST.get("artista")
        cancion = request.POST.get("cancion")
        tonalidad = request.POST.get("tonalidad")

        chart = ChartsMod(artista=artista, cancion=cancion, tonalidad=tonalidad)
        chart.save()

        return render(request, 'index.html')

    return render(request, 'charts.html')