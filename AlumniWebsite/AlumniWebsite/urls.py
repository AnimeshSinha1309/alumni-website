"""
Definition of urls for AlumniWebsite.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.conf.urls.static import static
from django.conf import settings

import app.forms
import app.views
import app.actions

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Primary Pages
    url(r'^$', app.views.home, name='home'),
    url(r'^events/$', app.views.events, name='events'),
    url(r'^alumni/$', app.views.alumni_batches, name='alumni'),
    url(r'^contribute/$', app.views.contribute, name='contribute'),
    url(r'^contact/$', app.views.contact, name='contact'),
    url(r'^school/$', app.views.school, name='school'),
    url(r'^team/$', app.views.team, name='team'),
    # Alumni listings and profiles
    url(r'^alumni/batch/$', app.views.alumni_batches, name='alumni/batches'),
    url(r'^alumni/circles/$', app.views.alumni_circles, name='alumni/circles'),
    url(r'^alumni/distinguished/$', app.views.alumni_distinguished, name='alumni/distinguished'),
    url(r'^alumni/search/$', app.views.alumni_search, name='alumni/search'),
    url(r'^alumni/batch/(?P<batch>[0-9]{4})/$', app.views.alumni_batchlist),
    url(r'^profile/(?P<username>\w*)/?$', app.views.profile, name='profile'),
    url(r'^settings/profile/edit/$', app.views.profile_edit, name='profile/edit'),
    url(r'^actions/befriend/(?P<username>\w*)/?$', app.actions.befriend),
    url(r'^actions/unfriend/(?P<username>\w*)/?$', app.actions.unfriend),
    # Authorization and Administration
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)