from django.urls import path
from sitio.views import (
    home_v, 
    producciones_v, 
    multitracks_v, 
    charts_v, 
    pruebas_v, 
    bPruebas_v,
    # CLASE 22
    leerCharts_v,
    eliminarCharts_v,
    MtList,
    MtDetail,
    MtCreate,
    MtUpdate,
    MtDelete,
    #CLASE 23
    login_request,
    register_v,
    LogoutView
)

urlpatterns = [
    path('', home_v, name='home'),
    path('producciones', producciones_v, name='producciones'),
    path('multitracks', multitracks_v, name='multitracks'),
    path('charts', charts_v, name='charts'),
    path('pruebas', pruebas_v, name='pruebas'),
    path('pruebas2', bPruebas_v, name='pruebas2'),
    #CLASE 22
    path('leer_charts', leerCharts_v, name='leer_charts'),
    path('eliminar_charts/<num_id>', eliminarCharts_v, name='eliminar_charts'),
    path('mt/list', MtList.as_view(), name='mtlist'),
    path('mt/detail/<pk>', MtDetail.as_view(), name='mtdetail'),
    path('mt/edit/<pk>', MtUpdate.as_view(), name='mtedit'),
    path('mt/delete/<pk>', MtDelete.as_view(), name='mtdelete'),
    path('mt/create', MtCreate.as_view(), name='mtcreate'),
    #CLASE 23
    path('login', login_request, name='login'),
    path('register', register_v, name='register'),
    path('logout', LogoutView.as_view(template_name = 'logout.html'), name='logout'),

]