from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

def index(request):
    return render(request, "index.html")
    # return HttpResponse('homepage made')

def about(request):
    return render(request, 'about.html')

def skills(request):
    return render(request, 'skills.html')

def work(request):
    return render(request, 'work.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, desc = desc, date = datetime.today() )
        contact.save()

    return render(request, 'contact.html')
