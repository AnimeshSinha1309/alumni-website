"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User


# Models about user and profile data.


class Alumnus(models.Model):
    class Meta:
        verbose_name_plural = "Alumni"
    def __str__(self):
        return self.user.username
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ## Displayed grouped as LGBTQ / Others
        ('L', 'Lesbian'),
        ('G', 'Gay'),
        ('B', 'Bisexual'),
        ('T', 'Transgender'),
        ('Q', 'Queer'),
    )
    RELATIONSHIP_CHOICES = (
        ('MR', 'Married'),
        ('SN', 'Single'),
        ('RL', 'In a Relationship'),
        ('DV', 'Divorced'),
    )
    VALIDITY_CHOICES = (
        ('V', 'Validated'),
        ('P', 'Paid'),
        ('U', 'Unchecked'),
        ('B', 'Blocked'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile/', default='profile/_defaultavatar.png')
    birth_date = models.DateField(null=True)
    jobtitle = models.CharField(max_length=50, null=True)
    workplace = models.CharField(max_length=100, null=True)
    batch = models.IntegerField(null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=True)
    admission_number = models.CharField(max_length=20, null=True)
    current_address = models.TextField(max_length=500, null=True)
    permanent_address = models.TextField(max_length=500, null=True)
    phone_mobile = models.CharField(max_length=20, null=True)
    phone_home = models.CharField(max_length=20, null=True)
    phone_work = models.CharField(max_length=20, null=True)
    relationship_status = models.CharField(max_length=2, null=True, choices=RELATIONSHIP_CHOICES)
    validity_code = models.CharField(max_length=1, choices=VALIDITY_CHOICES, default='U')


class Circle(models.Model):
    FRIENDSHIP_CHOICES = (
        ('FR', 'Friends'),
        ('AQ', 'Acquaintences'),
    )
    def __str__(self):
        return self.friend.user.username + ' is a friend of ' + self.user.user.username
    user = models.ForeignKey(Alumnus, related_name='alumnus_user')
    friend = models.ForeignKey(Alumnus, related_name='alumnus_friend')
    type = models.CharField(max_length=2, choices=FRIENDSHIP_CHOICES)


# Models about event and program data


class Event(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    description = models.TextField(max_length=2500)
    date = models.DateField()