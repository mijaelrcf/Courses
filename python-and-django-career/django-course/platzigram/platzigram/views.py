"""Platzigram URLs module."""
# Django
from django.http import HttpResponse
#from django.http import JsonResponse

# Utilities
from datetime import datetime
import json


def hello_world(request):
    """return a greeting."""    
    #return HttpResponse('Hello, world')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def sort_integers(request):
    """return a JSON response with sorted integers."""
    numbers = request.GET['numbers']
    #import pdb; pdb.set_trace()
    sorted_numbers = sorted([int(i) for i in numbers.split(',')])

    data = {
        'status': 'ok',
        'numbers': sorted_numbers,
        'message': 'Integers sorted successfully'
    }
    
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json'
    )
    #return HttpResponse(str(sorted_numbers), content_type='application/json')
    #return HttpResponse(JsonResponse({'sorted_number': sorted_numbers}))


def say_hi(request, name, age):
    """return a greeting."""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}: Welcome to Platzigram'.format(name)

    return HttpResponse(message)