from django.shortcuts import render, redirect

def index(request):
    return render (request,"index.html")

def login(request):
    return render (request,"login.html")

def QuieneSomos(request):
    return render (request,"QuieneSomos.html")

def tienda(request):
    return render (request,"tienda.html")
