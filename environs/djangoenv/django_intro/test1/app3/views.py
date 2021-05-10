from django.shortcuts import render, redirect



# Create your views here.
def homes(request):
    return render(request, "homes.html")


def doit(request):
    inputs = {
        "name" : request.POST["name"], 
        "lang" : request.POST["lang"], 
        "loca" : request.POST["loca"], 
        "comm" : request.POST["comm"],
        "hate" : request.POST["hate"], 
        "brows" : request.POST.getlist("brows")
        }

    return render(request, "results.html", inputs)
