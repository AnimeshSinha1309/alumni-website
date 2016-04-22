from django.shortcuts import redirect
from django.http import HttpRequest
from app.models import Alumnus, User, Circle

def befriend(request, username):
    """Adds a friend to the current user's profile."""
    assert isinstance(request, HttpRequest)
    if(not request.user.is_authenticated()):
        return redirect('/login/')
    befriender = Alumnus.objects.get(user = request.user)
    befriendee = Alumnus.objects.get(user = User.objects.get(username=username))
    if(befriender != befriendee and Circle.objects.filter(user=befriender, friend=befriendee).count() == 0):
        Circle(user=befriender, friend=befriendee, type='FR').save()
    return redirect('/profile/' + username,)

def unfriend(request, username):
    """Removes a friend from the current user's profile."""
    assert isinstance(request, HttpRequest)
    if(not request.user.is_authenticated()):
        return redirect('/login/')
    unfriender = Alumnus.objects.get(user = request.user)
    unfriendee = Alumnus.objects.get(user = User.objects.get(username=username))
    if(unfriender != unfriendee):
        Circle.objects.get(user=unfriender, friend=unfriendee).delete()
    return redirect('/profile/' + username,)