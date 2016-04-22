"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.db.models import Q
from datetime import datetime
from app.models import Alumnus, User, Circle

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

## Alumni Features and Profiles

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

def alumni_circles(request):
    """Renders the alumni listing for your circles."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/alumni_circles.html',
        {
            'title':'Your Alumni Circles',
            'people':Circle.objects.filter(user=Alumnus.objects.get(user=request.user)).only('friend'),
            'year':datetime.now().year,
        }
    )

def alumni_distinguished(request):
    """Renders the distinguished alumni page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/alumni_distinguished.html',
        {
            'title':'Our Distinguished Alumni',
            'year':datetime.now().year,
        }
    )

def alumni_search(request):
    """Renders the alumni search page."""
    assert isinstance(request, HttpRequest)
    fullresults = []
    if request.method == 'GET':
        results = []
        fullquery = request.GET.get('q', '_NOSTRINGMATCHUNIQUEDATAFLAGPASS12093232176')
        # Analyze each word of full query to get results
        assert isinstance(fullquery, str)
        for query in fullquery.split(' '):
            users = User.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
            alumni = Alumnus.objects.filter(Q(jobtitle__icontains=query) | Q(batch__iexact=query))
            for user in users:
                results.append(Alumnus.objects.get(user=user))
            for index in range(len(alumni)):
                results.append(alumni[index])
        # Add results after checking for result redundancies
        for result in results:
            if result not in fullresults:
                fullresults.append(result)
    return render(
        request,
        'app/alumni_search.html',
        {
            'title':'Search Alumni',
            'year':datetime.now().year,
            'results':fullresults
        }
    )

def profile(request, username):
    """Renders personal profiles."""
    assert isinstance(request, HttpRequest)
    # Getting Alumnus to be displayed on profile
    if(username == ""): person = request.user
    else: person = User.objects.get(username=username)
    displaying = Alumnus.objects.get(user=person)
    # Checking for Friendship status on Circles
    befriender = Alumnus.objects.get(user = request.user)
    befriendee = Alumnus.objects.get(user = person)
    if(Circle.objects.filter(user=befriender, friend=befriendee).count() != 0): status = 'Friends'
    elif(request.user == person): status = 'Self'
    else: status = 'Unconnected'
    # Rendering the view
    return render(
        request,
        'app/profile.html',
        {
            'title':'Alumni List',
            'data':displaying,
            'friends':Circle.objects.filter(user=displaying).only('friend'),
            'year':datetime.now().year,
            'status':status,
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