from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Tool(models.Model):
    tool_id = models.CharField(max_length=233)
    description = models.CharField(max_length=233)
    parts = models.CharField(max_length=233)
    brand = models.CharField(max_length=244)
    model = models.CharField(max_length=233)
    available = models.BooleanField(default=True)
    # borrower = models.CharField(max_length=233, null=True, default=True)  # TODO: LINK TO USERS (Done? see line below)
    borrower = models.ForeignKey(User)

    def __str__(self):
        return self.description


category_list = ["Automotive",
                 "Paint",
                 "Yard",
                 "Woodworking",
                 "Metalworking"]


class ToolCategory(models.Model):
    category = models.CharField(max_length=255)  # TODO:Link to category list

    def __str__(self):
        return self.category


class User(models.Model):
    def full_name_function(self):
        return "{} {}".format(self.first_name, self.last_name)
    user_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_created = models.DateField()
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, null=True, blank=True, default=False)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip = models.CharField(max_length=5)
    late_tools = models.BooleanField(default=False)


    def __str__(self):
        return self.first_name
