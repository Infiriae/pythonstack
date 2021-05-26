from django.shortcuts import render, redirect
from django.contrib import messages
from .modelsclass import *
from bcrypt import *


def index(request):
    return render(request,"index.html")

def success(request):

    if "user_id" not in request.session:
        return redirect('/')
    context = {
        "facebook_posts": Facebook_Post.objects.all
    }
    return render(request,"success.html",context)


def add_movie(request):
    errors = Movie.objects.validate(request.POST)

    if errors:
        for error in errors.values()
            messages.error(request,error)
        return redirect("/")

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

        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

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

            if bcrypt.checkpw(password.encode(),logged_user.password.encode()):
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
    else:
        return redirect('/')


def like(request,id):

    user = User.objects.get(id=request.session["user_logged_in"])

    quote = Quote.objects.get(id=id)

    quote.fans.add(user)

    movie_id = quote.movie.id

    return redirect(f'/quotes/{movie_id}')


def activity(request):
    context = {
    
    }
    return render(request,"activity.html",context)

def logout(request):

    request.session.flush()

    return redirect('/')

def create_post(request):
    
    message = request.POST['message']
    poster = User.objects.get(id=request.session['user_id'])
    Facebook_Post.objects.create(message=message,poster=poster)

    

    return redirect('/success')
    