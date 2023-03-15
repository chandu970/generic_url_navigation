from django.shortcuts import render

# Create your views here.
def Hero(request):
    return render(request,'Hero.html')

def Villan(request):
    return render(request,'Villan.html')