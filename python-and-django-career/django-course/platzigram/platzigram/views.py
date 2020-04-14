"""Platzigram URLs module."""
# Django
from django.http import HttpResponse
from django.http import JsonResponse

# Utilities
from datetime import datetime

def hello_world(request):
    """return a greeting."""    
    #return HttpResponse('Hello, world')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def hi(request):
    """Hi."""
    numbers = request.GET['numbers']
    sorted_number = sorted([int(x) for x in numbers.split(',')])
    #import pdb; pdb.set_trace()
    return HttpResponse(JsonResponse({'sorted_number': sorted_number}))
