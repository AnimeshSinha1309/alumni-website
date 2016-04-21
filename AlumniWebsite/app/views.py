"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Alumnus, User

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def events(request):
    """Renders the events page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/events.html',
        {
            'title':'Events Calender',
            'year':datetime.now().year,
        }
    )

def alumni_batches(request):
    """Renders the alumni batch listing."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/alumni_batches.html',
        {
            'title':'Alumni List',
            'batches':range(2016, 1981, -1),
            'year':datetime.now().year,
        }
    )

def alumni_batchlist(request, batch):
    """Renders the alumni batch listing."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/alumni_batchlist.html',
        {
            'title':'Alumni List',
            'batch':batch,
            'people':Alumnus.objects.filter(batch=int(batch)),
            'year':datetime.now().year,
        }
    )

def profile(request, username):
    """Renders personal profiles."""
    assert isinstance(request, HttpRequest)
    if(username == ""):
        person = request.user
    else:
        person = User.objects.get(username=username)
    return render(
        request,
        'app/profile.html',
        {
            'title':'Alumni List',
            'data':Alumnus.objects.get(user=person),
            'year':datetime.now().year,
        }
    )

def contribute(request):
    """Renders the contribute page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contribute.html',
        {
            'title':'Contribute to the School',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def school(request):
    """Renders the school page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/school.html',
        {
            'title':'St. Thomas Today',
            'year':datetime.now().year,
        }
    )