from django.shortcuts import render, redirect



# Create your views here.
def homes(request):
    return render(request, "homes.html")


def doit(request):

    request.session['name'] = request.POST['name']
    request.session["lang"] = request.POST["lang"]
    request.session["loca"] = request.POST["loca"]
    request.session["comm"] = request.POST["comm"]
    request.session["hate"] = request.POST["hate"]
    request.session["brows"] = request.POST.getlist("brows")
    request.session["browlen"] = len(request.session["brows"])-1
    request.session["browstyped"] = []
    for each in request.session["brows"]:
        if each == request.session["brows"][request.session["browlen"]]:
            teach = "and " + each + "."
            request.session["browstyped"].append(teach)
        else:
            teach = each + ", "
            request.session["browstyped"].append(teach)
    if len(request.session["browstyped"]) == 0:
        request.session["browstyped"].append("None Selected.")


    # inputs = {
    #     "name" : request.POST["name"], 
    #     "lang" : request.POST["lang"], 
    #     "loca" : request.POST["loca"], 
    #     "comm" : request.POST["comm"],
    #     "hate" : request.POST["hate"], 
    #     "brows" : request.POST.getlist("brows")
    #     }

    return redirect("/results")

def done(request):
    return render(request, "results.html")