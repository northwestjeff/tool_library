from django.db import models
from django.contrib.auth.models import User, AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver


category_list = (
    ("Automotive", "automotive"),
    ("Paint", "paint"),
    ("Yard", "yard"),
    ("Woodworking", 'woodworking'),
    ("Metalworking", "metalworking"))

# class Profile(models.Model):
#     user = models.OneToOneField(User)
#     bio = models.TextField(blank=True)
#     location = models.CharField(max_length=100)
#     birth_date = models.DateField(null=True, blank=True)

# from django.db import models
# from django.contrib.auth.models import AbstractUser
#
# class User(AbstractUser):
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)

class User(AbstractUser):
    is_member = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    date_created = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)
    late_tools = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name



# class Profile(models.Model):
#     user = models.OneToOneField(User)
#     # user_id = models.CharField(max_length=50)
#     is_member = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_created = models.DateField()
#     email = models.CharField(max_length=50)
#     zip = models.CharField(max_length=5)
#     late_tools = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.user.first_name


class Tool(models.Model):
    tool_id = models.IntegerField(unique=True)  # TODO need to keep this to five numbers
    description = models.CharField(max_length=144)
    parts = models.CharField(max_length=144)
    brand = models.CharField(max_length=144)
    model = models.CharField(max_length=144)
    available = models.BooleanField(default=True)
    user = models.ForeignKey(User, null=True, blank=True)
    category = models.CharField(choices=category_list, null=True, blank=True, max_length=200)

    def __str__(self):
        return self.description


class Comment(models.Model):
    user = models.ForeignKey(User)
    tool = models.ForeignKey(Tool)
    comment = models.TextField(max_length=288, blank=True, null=True)
    date = models.DateField()


class Activity(models.Model):
    user = models.ForeignKey(User)
    tool = models.ForeignKey(Tool)
    action = models.CharField(max_length=50)
    date_out = models.DateField()
    date_in = models.DateField()


# class Activity(models.Model):

