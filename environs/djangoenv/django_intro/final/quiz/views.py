from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"],
        "app" : "app2"
    }
    return render(request, "index.html", context)