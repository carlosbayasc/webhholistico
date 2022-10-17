from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,"core/home.html")
    
def nosotros(request):
    return render(request,"core/nosotros.html")

def terapias(request):
    return render(request,"core/terapias.html")

def contacto(request):
    return render(request,"core/contactos.html")