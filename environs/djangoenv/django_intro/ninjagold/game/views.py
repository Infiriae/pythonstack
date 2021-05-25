from django.shortcuts import render, redirect
from random import randint
from time import localtime, strftime

# Create your views here.
def index(request):
    if request.session['cash'] is None:
        request.session['cash'] = 300
        request.session['count'] = 0
        request.session['realism'] = []
        request.session['loge'] = []
        request.session['goals'] = 600
    else:
        goals = request.session['goals']
        if request.session['cash'] > goals:
            return redirect("/winner")
    return render(request, "index.html")

def obje(request):
    return redirect("/")
def wins(request):
    logs = []
    cash = 0
    moves = 0
    cash = request.session['cash']
    moves = request.session['count']
    logs.append("You won with " + str(cash) + " gold in " + str(moves) + " moves! " + strftime("%Y-%m-%d %H:%M %p", localtime()) )
    request.session['loge'] = logs
    request.session['cash'] = 0
    request.session['count'] = 0
    return redirect("/")

def play(request,id):
    if id == 1:
        realism2 = []
        logs = []
        logs = request.session['loge']
        request.session['cash'] = request.session['cash'] - 1
        request.session['count'] = request.session['count'] + 1
        realism2 = request.session['realism']
        realism2.append(request.session['count'])
        request.session['realism'] = realism2
        logs.insert(0,"You paid one gold. " + strftime("%Y-%m-%d %H:%M %p", localtime()))
        request.session['loge'] = logs
    elif id == 2:
        realism2 = []
        logs = []
        win = randint(10,20)
        request.session['cash'] = request.session['cash'] + win
        request.session['count'] = request.session['count'] + 3
        realism2 = request.session['realism']
        logs = request.session['loge']
        realism2.append(request.session['count'])
        request.session['realism'] = realism2
        logs.insert(0,"You made " + str(win) + " gold farming. " +strftime("%Y-%m-%d %H:%M %p", localtime()))
        request.session['loge'] = logs
    elif id == 3:
        realism2 = []
        logs = []
        win = randint(5,10)
        request.session['cash'] = request.session['cash'] + win
        request.session['count'] = request.session['count'] + 2
        realism2 = request.session['realism']
        logs = request.session['loge']
        realism2.append(request.session['count'])
        request.session['realism'] = realism2
        logs.insert(0,"You made " + str(win) + " gold exploring a cave. " +strftime("%Y-%m-%d %H:%M %p", localtime()))
        request.session['loge'] = logs
    elif id == 4:
        realism2 = []
        logs = []
        win = randint(2,5)
        request.session['cash'] = request.session['cash'] + win
        request.session['count'] = request.session['count'] + 1
        realism2 = request.session['realism']
        logs = request.session['loge']
        realism2.append(request.session['count'])
        request.session['realism'] = realism2
        logs.insert(0,"You made " + str(win) + " gold exploring cleaning the house. " +strftime("%Y-%m-%d %H:%M %p", localtime()))
        request.session['loge'] = logs
    elif id == 5:
        if request.session['cash'] < 50:
            logs = []
            logs = request.session['loge']
            logs.insert(0,"You don't have enough gold to gamble.")
            request.session['loge'] = logs
            return redirect("/")
        realism2 = []
        logs = []
        win = randint(-50,50)
        request.session['cash'] = request.session['cash'] + win
        request.session['count'] = request.session['count'] + 1
        realism2 = request.session['realism']
        logs = request.session['loge']
        realism2.append(request.session['count'])
        request.session['realism'] = realism2
        if win > 0:
            logs.insert(0,"You made " + str(win) + " gold gambling at the casino! " +strftime("%Y-%m-%d %H:%M %p", localtime()))
        else:
            logs.insert(0,"You lost " + str(win*-1) + " gold gambling at the casino! " +strftime("%Y-%m-%d %H:%M %p", localtime()))
        request.session['loge'] = logs
    return redirect("/")

def new(request):
    request.session.flush()
    request.session['cash'] = 300
    request.session['count'] = 0
    request.session['realism'] = []
    request.session['loge'] = []
    request.session['goals'] = 600
    return redirect("/")