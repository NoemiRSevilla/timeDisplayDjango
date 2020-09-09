from django.shortcuts import render, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    if 'counter' not in request.request.session:
        request.session['counter'] = 0
    else:
        request.session['counter']+=1
    context = {
        'string': get_random_string(length=14)
    }
    return render(request, "random.html", context)

def destroy(request):
    del request.session['counter']
    return render(request, "random.html")