from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required

# Vista para la página de inicio
def index(request):
    # Renderiza la plantilla 'index.html'
    return render(request, 'index.html')

# Vista para agregar un vehículo
# Requiere que el usuario esté autenticado (login_required)
# y que tenga el permiso 'vehiculo.agregar_vehiculo' (permission_required)
@login_required
@permission_required('vehiculo.agregar_vehiculomodel', raise_exception=True)
def add_vehiculo(request):
    # Si la petición es POST (el formulario ha sido enviado)
    if request.method == 'POST':
        # Crea un formulario con los datos enviados
        form = VehiculoForm(request.POST)
        # Si el formulario es válido, guarda el vehículo
        if form.is_valid():
            form.save()
            # Redirige a la página de listado de vehículos después de agregar
            return redirect('list_vehiculo')
    else:
        # Si la petición no es POST (es GET), se crea un formulario vacío
        form = VehiculoForm()
    # Renderiza la plantilla 'add_vehiculo.html' con el formulario
    return render(request, 'add_vehiculo.html', {'form': form})



# Vista para listar los vehículos
# Requiere que el usuario esté autenticado (login_required)
# y que tenga el permiso 'vehiculo.visualizar_catalogo' (permission_required)
@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def list_vehiculo(request):
    # Obtiene todos los vehículos de la base de datos
    vehiculos = Vehiculo.objects.all()
    # Renderiza la plantilla 'list_vehiculo.html' con la lista de vehículos
    return render(request, 'list_vehiculo.html', {'vehiculos': vehiculos})

# Vista para listar los vehículos
# Requiere que el usuario esté autenticado (login_required)
# y que tenga el permiso 'vehiculo.visualizar_catalogo' (permission_required)
@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def list_vehiculo(request):
    # Obtiene todos los vehículos de la base de datos
    vehiculos = Vehiculo.objects.all()
    # Renderiza la plantilla 'list_vehiculo.html' con la lista de vehículos
    return render(request, 'list_vehiculo.html', {'vehiculos': vehiculos})

def switch_user(request, username):
    try:
        # Busca el usuario en la base de datos
        user = User.objects.get(username=username)
        # Inicia sesión en el usuario
        login(request, user)
        # Redirige a la vista de inicio
        return redirect('/') 
    except User.DoesNotExist:
        return HttpResponse("Usuario no encontrado", status=404)