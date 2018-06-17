from django.shortcuts import render, redirect

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

def family_rehearsal(request):
    return render(request, 'family-rehearsal.html')

def family(request):
    return render(request, 'family.html')

def dinner(request):
    return render(request, 'rehearsal-dinner.html')

def vote(request):
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSeYlzXYbE0QUkTYdud8poQri-tkWyf4H5-KReFAA3kLa52rcw/viewform")
