from django.urls import path
from . import views

urlpatterns = [
    # URLs de autenticación
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_usuario, name='registro'),
    path('users/', views.users_list, name='users_list'),

    # Nuevas URLs de la biblioteca
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/<int:libro_id>/', views.detalle_libro, name='detalle_libro'),
]