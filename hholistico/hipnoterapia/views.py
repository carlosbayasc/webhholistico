from django.shortcuts import render
from .models import Hipnoterapia

# Create your views here.
def hipnoterapia(request):
    hipnoterapias= Hipnoterapia.objects.all()
    return render(request,"hipnoterapia/hipnoterapia.html",{'hipnoterapias':hipnoterapias})