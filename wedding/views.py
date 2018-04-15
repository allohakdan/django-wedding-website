from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

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