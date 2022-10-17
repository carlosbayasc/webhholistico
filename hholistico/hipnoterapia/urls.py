from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    # Path del Nucleo
    path('', views.hipnoterapia,name="hipnoterapia"),

    #path del admin
    path('admin/', admin.site.urls),
]