from django.shortcuts import render
from .models import Elybra

# Create your views here.
def elybra(request):
    elybras = Elybra.objects.all()
    return render(request,"elybra/elybra.html",{'elybras':elybras})