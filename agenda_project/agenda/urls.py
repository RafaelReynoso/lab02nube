from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home),
    path('registrarContacto/', views.registrarContacto),
    path('edicionContacto/<codigo>',views.edicionContacto),
    path('editarContacto/', views.editarContacto),
    path('eliminacionContacto/<codigo>', views.eliminarContacto),
]