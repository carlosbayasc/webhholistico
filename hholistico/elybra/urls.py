from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    # Path del Nucleo
    path('', views.elybra,name="elybra"),

    #path del admin
    path('admin/', admin.site.urls),
]