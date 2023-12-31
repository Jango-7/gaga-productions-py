# from django.shortcuts import render
from django.shortcuts import render
from .models import ProduccionesMod, MultitracksMod, ChartsMod

def home_v(request):
    return render(request, 'index.html')

def producciones_v(request):
    return render(request, 'producciones.html')

def multitracks_v(request):
    return render(request, 'multitracks.html')

def charts_v(request):
    return render(request, 'charts.html')