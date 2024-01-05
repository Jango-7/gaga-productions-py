from django.urls import path
from sitio.views import home_v, producciones_v, multitracks_v, charts_v #find_v

urlpatterns = [
    path('', home_v, name='home'),
    path('producciones', producciones_v, name='producciones'),
    path('multitracks', multitracks_v, name='multitracks'),
    path('charts', charts_v, name='charts'),
    # path('find_charts', find_v, name='find'),
]