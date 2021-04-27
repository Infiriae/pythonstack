from django.shortcuts import render
from time import localtime, strftime

def index(request):
    context = {
        "name": "Collette",
        "favorite_color": "Green",
        "pets": ["Alice", "Jamie", "Leanna"],
        "app" : "Time App front"
    }
    return render(request, "index.html", context)


def time(request):
    context = {
        "date": strftime("%Y-%m-%d", localtime()),
        "time": strftime("%H:%M %p", localtime()),
        "app" : "Time App clock"
    }
    return render(request,'time.html', context)
