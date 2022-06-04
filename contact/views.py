from django.shortcuts import render
from .forms import ContactForm
from .models import *

# Create your views here.


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    ctx = {
        'form': form
    }
    return render(request, 'contact.html', ctx)


def about(request):
    teams = Team.objects.all()
    ctx = {
        'teams': teams
    }
    return render(request, 'about.html', ctx)
