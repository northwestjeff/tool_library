from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.timezone import now
import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver


category_list = (
    ("Automotive", "automotive"),
    ("Paint", "paint"),
    ("Yard", "yard"),
    ("Woodworking", 'woodworking'),
    ("Metalworking", "metalworking"))

class User(AbstractUser):
    is_member = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    date_created = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)
    late_tools = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name


class Tool(models.Model):
    tool_id = models.IntegerField(unique=True)  # TODO need to keep this to five numbers
    description = models.CharField(max_length=144)
    parts = models.CharField(max_length=144)
    brand = models.CharField(max_length=144)
    model = models.CharField(max_length=144)
    available = models.BooleanField(default=True)
    date_out = models.DateField(blank=True, null=True)
    date_due = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True)
    category = models.CharField(choices=category_list, null=True, blank=True, max_length=200)
    # TODO IF CHECKED OUT NEED TO ADD A DATE CHECKED OUT FIELD TO TOOL

    def __str__(self):
        return self.description


class Comment(models.Model):
    user = models.ForeignKey(User)
    tool = models.ForeignKey(Tool)
    comment = models.TextField(max_length=288, blank=True, null=True)
    date = models.DateField()


class Activity(models.Model):
    member = models.ForeignKey(User, blank=True, null=True)
    staff = models.CharField(max_length=50, blank=True, null=True)
    tool = models.ForeignKey(Tool, blank=True, null=True)
    action = models.CharField(max_length=50)
    date_out = models.DateField(blank=True, null=True)
    date_in = models.DateField(blank=True, null=True)



