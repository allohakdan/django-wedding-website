from django.shortcuts import render
from guests.save_the_date import SAVE_THE_DATE_CONTEXT_MAP


def home(request):
    return render(request, 'home.html', context={
        'save_the_dates': SAVE_THE_DATE_CONTEXT_MAP
    })

def when(request):
    return render(request, 'when.html')

def where(request):
    return render(request, 'where.html')

def why(request):
    return render(request, 'why.html')

def how(request):
    return render(request, 'how.html')

def wedding_party(request):
    return render(request, 'wedding-party.html')