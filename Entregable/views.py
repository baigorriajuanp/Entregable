from asyncore import read
from django.template import Template, Context
from django.http import HttpResponse 
from django.shortcuts import render
from .forms import FamiliarForm
from .models import Familiar

from Entregable.forms import FamiliarForm

def familia_completa(request):
    #return (HttpResponse(f"FAMILIA COMPLETA"))
    return render(request,"html_familia_completa.html")


def findfamiliar (request):
    return render(request,"findfamiliar.html")
    #return (HttpResponse(f"ENCONTRAR UN FAMILIAR"))


def familiarForm (request):
    if request.method == "POST":
        myform = FamiliarForm(request.POST)
        if myform.is_valid:
            print(myform)
            familiar_data = myform.cleaned_data
            familiar = Familiar(name = familiar_data["name"], surname = familiar_data["surname"], age = familiar_data["age"], birth_date = familiar_data["birth_date"], link = familiar_data["link"])
            familiar.save()
            return HttpResponse(F"Familiar creado")
    else:
        myform = FamiliarForm()
        print("*********************************************")
    return render (request,"familiarform.html",{"myform":myform})

