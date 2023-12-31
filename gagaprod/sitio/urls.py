from django.urls import path
from sitio.views import home_v, producciones_v, multitracks_v, charts_v

urlpatterns = [
    path('', home_v),
    path('producciones', producciones_v),
    path('multitracks', multitracks_v),
    path('charts', charts_v),
]