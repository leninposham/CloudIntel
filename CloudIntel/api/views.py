from django.shortcuts import render

# Create your views here.
def API_UI(request):
    return render(request,"api/apifrontend.html",{})