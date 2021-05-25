from django.shorcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt


def index(request):
    return render(request,"index.html")

def success(request):

    if "user_id" not in request.session:
        return redirect('/')

    return render(request,"success.html")

def register(request):

    if request.method == "POST":
        errors = User.objects.validate()

        if errors:
            for error in errors.values():
                messages.error(request,error)
            return redirect('/')


        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        pw_hash = bcrypt.hashpw(password.encode(), bcrpyt.gensalt()).decode()

        user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash)

        request.session['user_id'] = user.id
        request.session['user_name'] = f"{user.first_name} {user.last_name}"


        return redirect('/success')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        logged_user = User.objects.filter(email=email)
        
        if logged_user:
            
            logged_user = logged_user[0]

            if bcrypt.checkpw(password.encode(),logged_user.password.encode())
            if logged_user.password == password:
                request.session['user_id'] = logged_user.id
                request.session['user_name'] = f"{logged_user.first_name} {logged_user.last_name}"
                return redirect('/success')
            else:
                messages.error(request,"Incorrect password entered")
                return redirect('/')
        else:
            messages.error(request,"This user doesn't exist")
            return redirect('/')
    return redirect('/')

def logout(request):

    request.session.flush()

    return redirect('/')