from django.shortcuts import render

def accueil(request):
        return render(request,'ludo/accueil.html')