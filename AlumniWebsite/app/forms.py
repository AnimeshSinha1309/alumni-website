"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class ProfileEditingForm(forms.Form):
    fname = forms.CharField(max_length=100,
                            label='First Name',
                            widget=forms.TextInput({
                                'class': 'form-control',
                                'placeholder': 'First name'}))
    lname = forms.CharField(max_length=100,
                            label='Last Name',
                            widget=forms.TextInput({
                                'class': 'form-control',
                                'placeholder': 'Last name'}))
    jobtitle = forms.CharField(max_length=100,
                               label='Jobtitle',
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Your Designation at work'}))
    workplace = forms.CharField(max_length=100,
                                label='Workplace',
                                widget=forms.TextInput({
                                    'class': 'form-control',
                                    'placeholder': 'The name of Your Office'}))
    email = forms.EmailField(max_length=100,
                             label='Email Address',
                             widget=forms.EmailInput({
                                 'class': 'form-control',
                                 'placeholder': 'eg. someone@example.com'}))
    birth_date = forms.DateField(label='Birth Date',
                                 widget=forms.SelectDateWidget({
                                     'class': 'form-control date-selector',
                                     }, years=range(1950, 2020)))
    current_address = forms.CharField(label='Current Address',
                                      widget=forms.Textarea({
                                          'class': 'form-control textarea-selector',
                                          'placeholder': 'Type in your present address'}))
    permanent_address = forms.CharField(label='Permanent Address',
                                        widget=forms.Textarea({
                                            'class': 'form-control textarea-selector',
                                            'placeholder': 'Type in your permanent address'}))
    phone_mobile = forms.IntegerField(label='Mobile No.',
                                      widget=forms.TextInput({
                                          'class': 'form-control',
                                          'placeholder': 'eg. +91 00000 00000'}))
    phone_home = forms.IntegerField(label='Personal Phone',
                                    widget=forms.TextInput({
                                        'class': 'form-control',
                                        'placeholder': 'eg. +91 00000 00000'}))
    phone_work = forms.IntegerField(label='Work Contact',
                                    widget=forms.NumberInput({
                                        'class': 'form-control',
                                        'placeholder': 'eg. +91 00000 00000'}))
    relationship_status = forms.ChoiceField(choices=(('MR', 'Married'), ('SN', 'Single'),
        ('RL', 'In a Relationship'), ('DV', 'Divorced'),),
                                            widget=forms.RadioSelect({
                                                'class': 'form-control choice-selector'}))