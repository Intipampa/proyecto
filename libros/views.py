from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Libro, Prestamo  # <-- Importa el modelo Prestamo
from .forms import LibroForm , CustomUserCreationForm

def is_superuser(user):
    return user.is_superuser

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser:
                return redirect('users_list') 
            else:
                return redirect('lista_libros')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required 
@user_passes_test(is_superuser) 
def users_list(request):
    # Obtiene todos los usuarios y precarga sus préstamos
    users = User.objects.all().prefetch_related('prestamo_set')
    return render(request, 'users_list.html', {'users': users})

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})

def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    return render(request, 'detalle_libro.html', {'libro': libro})
def registro_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid():
            user = form.save()
            user.email = form.cleaned_data.get('email')
            user.save()
            return redirect('login') 
    else:
        form = CustomUserCreationForm() 
    
    return render(request, 'registro.html', {'form': form})