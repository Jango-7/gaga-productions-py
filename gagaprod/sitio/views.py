# from django.shortcuts import render
from django.shortcuts import render
from .models import ProduccionesMod, MultitracksMod, ChartsMod
from sitio.forms import SearchForm

# ============= VISTA HOME ================

def home_v(request):
    form = SearchForm(request.GET)
    results = None

    if form.is_valid():
        query = form.cleaned_data['query']
        # Realiza la búsqueda en tu modelo
        results = ChartsMod.objects.filter(artista__icontains=query)

    return render(request, 'index.html', {"form":form, "results":results})

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


# ============ VISTA FIND =========

# def find_v(request):

#     if request.method == "GET":
#         artista = request.GET.get("artista")
#         cancion = request.GET.get("cancion")
#         tonalidad = request.GET.get("tonalidad")


#     return render(request, 'charts.html', {"artista":artista, "cancion":cancion, "tonalidad":tonalidad})


# def find_v(request):

#     if request.method == "GET":
#         artista = request.GET.get("artista")
#         cancion = request.GET.get("cancion")
#         tonalidad = request.GET.get("tonalidad")

#         if artista or cancion or tonalidad is None:
#             return 


#     return render(request, 'charts.html')