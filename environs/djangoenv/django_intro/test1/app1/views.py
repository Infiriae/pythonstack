from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("Placeholder to later display all blogs. <div><a href=\"/new\">To New placeholder</a></div><div><a href=\"/15\">To show 15 placeholder</a></div><div><a href=\"/15/edit\">To edit 15 placeholder</a></div>")
    #return HttpResponse("<a href=\"/index\">I</a> am ready to handle a request for '/'! <div><ul><li><form label=\"name\"><input text=\"Bear?\" id=\"bears\"><submit label=\"name\" text=\"Bears Name\"></form></li><li>Ok</li></ul></div>")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog<div><a href=\"/\">To home placeholder</a></div>")

def create(request):
    return redirect('/')

def show(request, num):
    return HttpResponse(f"placeholder to display blog number: {num}<div><a href=\"/\">To home placeholder</a></div>")

def edit(request, num):
    return HttpResponse(f"placeholder to edit blog number: {num}<div><a href=\"/\">To home placeholder</a></div>")

def destroy(request):
    return redirect('/')

def one_method(request):                #no values passed via URL
    return HttpResponse("I have a bear")
    pass
    
def another_method(request, my_val):    # my_val would be a number from the URL
    return HttpResponse(f'I have {my_val} bears')
    pass    # given the example above, my_val would be 23
    
def yet_another(request, name): # name would be a string from the URL
    return HttpResponse(f'I have a bear named {name}')
    pass    # given the example above, name would be 'pooh'
    
def one_more(request, id, color):   # id would be a number, and color a string from the URL
    return HttpResponse(f'Bear #{id} is {color} and it is perfect')
    pass    # given the example above, id would be 17 and color would be 'brown'