from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


# Create your views here.
def root(request):
    if request.session['count'] is None:
        request.session['count'] = 0
    return render(request, "rword.html")

def doit(request):
    request.session['count'] = 1 + int(request.session['count'])
    request.session['rword'] = get_random_string(length=14)
    return redirect("/rword")

def flushout(request):
    request.session.flush()
    request.session['count'] = 0
    return redirect("/rword")