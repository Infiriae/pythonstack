from django.shortcuts import render, HttpResponse
def index(request):
    
    return HttpResponse("<a href=\"/index\">I</a> am ready to handle a request for '/'! <div><ul><li><form label=\"name\"><input text=\"Bear?\" id=\"bears\"><submit label=\"name\" text=\"Bears Name\"></form></li><li>Ok</li></ul></div>")

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