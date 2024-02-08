# from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ProduccionesMod, MultitracksMod, ChartsMod
from sitio.forms import SearchForm, Formulario, UserRegistrationForm, UserEditForm
# CLASE 22
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#CLASE 23
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required


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

@login_required
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

@login_required
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

@login_required
def charts_v(request):
    if request.method == "POST":
        artista = request.POST.get("artista")
        cancion = request.POST.get("cancion")
        tonalidad = request.POST.get("tonalidad")

        chart = ChartsMod(artista=artista, cancion=cancion, tonalidad=tonalidad)
        chart.save()

        return render(request, 'index.html')

    return render(request, 'charts.html')


# ======= Vista about =======

def about_v(request):
    pass
    return render(request, 'about.html')


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

# PROOF

def pruebas_v(request):

    formu = Formulario()
    return render(request, 'pruebas.html', {"formu":formu})

def bPruebas_v(request):
    
    if request.method == 'GET':
        email = request.GET.get("email")
        cliente = None

        if email is None:
            return HttpResponse("Debe enviar un Email")
        
        cliente = ProduccionesMod.objects.filter(email=email)

        return render(request, 'pruebas2.html', {"cliente":cliente})
    


# ====== CLASE 22 ========
    


def leerCharts_v(request):

    charts = ChartsMod.objects.all()

    return render(request, 'leer_charts.html', {"charts": charts})


# --- INVESTIGACION SOBRE COMO LEER EL CAMPO POR EL ID ---

def eliminarCharts_v(request, num_id):
    
    chart = get_object_or_404(ChartsMod, id=num_id)
    chart.delete()

    charts = ChartsMod.objects.all()
    return render(request, 'leer_charts.html', {"charts": charts})


# ---- VISTAS BASADAS EN CLASES ----- 

class MtList(ListView):
    model = MultitracksMod
    template_name = 'mt_list.html'


class MtDetail(DetailView):
    model = MultitracksMod
    template_name = 'mt_detail.html'
    context_object_name = 'mt'

class MtCreate(CreateView):
    model = MultitracksMod
    fields = ['artista', 'cancion', 'descripcion']
    template_name = 'mt_form.html'
    success_url = '/sitio/mt/list'

class MtUpdate(UpdateView):
    model = MultitracksMod
    fields = ['artista', 'cancion', 'descripcion']
    template_name = 'mt_form.html'
    success_url = "/sitio/mt/list"

class MtDelete(DeleteView):
    model = MultitracksMod
    template_name = 'mt_delete.html'
    success_url = "/sitio/mt/list"


# ====== CLASE 23 ============

# ------ LOGIN ------
def login_request(request):

    if request.method == 'POST':
        #Leer los datos del form
        form = AuthenticationForm(request, data=request.POST)
        #Leer si los datos concuerdan con campos del form
        if form.is_valid():
            #Obtener los datos
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Usamos la funcion authenticate para validar si coinciden los datos de usuario y contraseña
            user = authenticate(username=username, password=password)
            # Si no coinciden, aparece un None, por lo tanto, si no es None, estas dentro. 
            if user is not None:
                login(request, user)
                return render(request, 'index.html', {"mensaje": f"Bienvenido {username}"})
            else:
                return render(request, 'index.html', {"mensaje": f"User or password wrong"})
        # Si los datos del form no son bien completados
        else:
            return render(request, 'index.html', {"mensaje": "Datos del formulario incorrectos"})        
    
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})


# ----- Registrar user ----- 

# def register_v(request):
#     if request.method == "POST":
#         # leer los datos que vienen del request.POST
#         form = UserCreationForm(request.POST)
#         # Validamos y guardamos los datos. Django se encarga de validar si la confirmacion de la contraseña es correcta.
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             form.save()
#             # importamos: from django.contrib import messages
#             messages.success(request, f"{username} registrado exitosamente")
#             # Redireccionamos a home con la funcion importada
#             return redirect('home')
#     else:
#         form = UserCreationForm()
    
#     return render(request, "registro.html", {"form": form})


# ---- CLASE 24 ------- registrar y editar user

def register_v(request):
    if request.method == "POST":
        # leer los datos que vienen del request.POST
        form = UserRegistrationForm(request.POST)
        # Validamos y guardamos los datos. Django se encarga de validar si la confirmacion de la contraseña es correcta.
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            # importamos: from django.contrib import messages
            messages.success(request, f"{username} registrado exitosamente")
            # Redireccionamos a home con la funcion importada
            return redirect('home')
    else:
        form = UserRegistrationForm()
    
    return render(request, "registro.html", {"form": form})


# ---- edit user ----
@login_required
def edit_user(request):
    
    usuario = request.user

    if request.method == 'POST':
        formulario = UserEditForm(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data
            usuario.email = info.get('email')
            usuario.password1 = info.get('password1')
            usuario.password2 = info.get('password2')
            usuario.last_name = info.get('last_name')
            usuario.first_name = info.get('first_name')

            usuario.save()
            return render(request, 'index.html')
    else:
        formulario = UserEditForm(initial={'email': usuario.email})

        return render(request, 'edit_user.html', {'formulario':formulario, 'usuario': usuario})