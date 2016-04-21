"""
Definition of urls for AlumniWebsite.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

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
    # Alumni listings
    url(r'^alumni/batch/$', app.views.alumni_batches, name='alumni/batches'),
    url(r'^alumni/batch/(?P<batch>[0-9]{4})/$', app.views.alumni_batchlist, name='alumni/batchlist'),
    url(r'^profile/(?P<username>\w*)/?$', app.views.profile, name='profile'),
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
]
