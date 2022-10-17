from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name="home"),
    path('nosotros/',views.nosotros,name="nosotros"),
    path('terapias/',views.terapias,name="terapias"),
    path('contacto/',views.contacto,name="contacto"),
]