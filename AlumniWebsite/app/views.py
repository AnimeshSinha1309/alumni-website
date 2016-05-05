"""
Definition of views.
"""

from datetime import datetime, date

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from app.models import Alumnus, User, Circle, Event
from app.forms import ProfileEditingForm


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


def events(request):
    """Renders the events page."""
    future_events = Event.objects.filter(date__gte=date.today()).order_by('date')
    past_events = Event.objects.filter(date__lt=date.today()).order_by('-date')
    if future_events:
        main_event = future_events[0]
    else:
        main_event = past_events[0]
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/events.html',
        {
            'title': 'Events Calender',
            'year': datetime.now().year,
            'main_event': main_event,
            'future_events': future_events[1:],
            'past_events': past_events,
        }
    )


def team(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/team.html',
        {
            'title': 'Our Team',
            'year': datetime.now().year,
        }
    )


# # Alumni Features and Profiles


def alumni_batches(request):
    """Renders the alumni batch listing."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/alumni_batches.html',
        {
            'title': 'Alumni List',
            'batches': range(2016, 1981, -1),
            'year': datetime.now().year,
        }
    )


def alumni_batchlist(request, batch):
    """Renders the alumni batch listing."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/alumni_batchlist.html',
        {
            'title': 'Alumni List',
            'batch': batch,
            'people': Alumnus.objects.filter(batch=int(batch)),
            'year': datetime.now().year,
        }
    )


@login_required
def alumni_circles(request):
    """Renders the alumni listing for your circles."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/alumni_circles.html',
        {
            'title': 'Your Alumni Circles',
            'people': Circle.objects.filter(user=Alumnus.objects.get(user=request.user)).only('friend'),
            'year': datetime.now().year,
        }
    )


def alumni_distinguished(request):
    """Renders the distinguished alumni page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/alumni_distinguished.html',
        {
            'title': 'Our Distinguished Alumni',
            'year': datetime.now().year,
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
            'title': 'Search Alumni',
            'year': datetime.now().year,
            'results': fullresults
        }
    )


@login_required
def profile(request, username):
    """Renders personal profiles."""
    assert isinstance(request, HttpRequest)
    # Getting Alumnus to be displayed on profile
    if username == "":
        person = request.user
    else:
        person = User.objects.get(username=username)
    displaying = Alumnus.objects.get(user=person)
    # Checking for Friendship status on Circles
    befriender = Alumnus.objects.get(user=request.user)
    befriendee = Alumnus.objects.get(user=person)
    if Circle.objects.filter(user=befriender, friend=befriendee).count() != 0:
        status = 'Friends'
    elif request.user == person:
        status = 'Self'
    else:
        status = 'Unconnected'
    # Rendering the view
    return render(
        request,
        'app/profile.html',
        {
            'title': 'Alumni List',
            'data': displaying,
            'friends': Circle.objects.filter(user=displaying).only('friend'),
            'year': datetime.now().year,
            'status': status,
        }
    )


@login_required
def profile_edit(request):
    """Renders personal profiles."""
    assert isinstance(request, HttpRequest)
    user = request.user
    profile = Alumnus.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileEditingForm(request.POST)
        if form.is_valid():
            profile.jobtitle = form.cleaned_data['jobtitle']
            profile.workplace = form.cleaned_data['workplace']
            profile.birth_date = form.cleaned_data['birth_date']
            profile.current_address = form.cleaned_data['current_address']
            profile.permanent_address = form.cleaned_data['permanent_address']
            profile.phone_mobile = form.cleaned_data['phone_mobile']
            profile.phone_home = form.cleaned_data['phone_home']
            profile.phone_work = form.cleaned_data['phone_work']
            profile.relationship_status = form.cleaned_data['relationship_status']
            user.first_name = form.cleaned_data['fname']
            user.last_name = form.cleaned_data['lname']
            user.email = form.cleaned_data['email']
            profile.save()
            user.save()
            return redirect('home')
    else:
        form = ProfileEditingForm(initial={'fname': request.user.first_name, 'lname': request.user.last_name,
                                           'jobtitle': profile.jobtitle, 'workplace': profile.workplace,
                                           'email': request.user.email,
                                           'birth_date': profile.birth_date, 'current_address': profile.current_address,
                                           'permanent_address': profile.permanent_address,
                                           'phone_mobile': profile.phone_mobile,
                                           'phone_home': profile.phone_home, 'phone_work': profile.phone_work,
                                           'picture': profile.picture,
                                           'relationship_status': profile.relationship_status})
    return render(
        request,
        'app/profile_edit.html',
        {
            'form': form,
            'title': 'Edit Your Profile',
            'year': datetime.now().year,
        }
    )


def contribute(request):
    """Renders the contribute page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contribute.html',
        {
            'title': 'Contribute to the School',
            'year': datetime.now().year,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Contact Us',
            'message': 'The Alumni Association',
            'year': datetime.now().year,
        }
    )


def school(request):
    """Renders the school page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/school.html',
        {
            'title': 'St. Thomas Today',
            'year': datetime.now().year,
        }
    )