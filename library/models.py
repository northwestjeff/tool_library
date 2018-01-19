from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator

# def validateToolId(value):
#     if len(value) != 5:
#         raise ValidationError(
#             _('Tool IDs must be exactly 5 numbers')
#         )
category_list = (
    ("Automotive", "automotive"),
    ("Paint", "paint"),
    ("Yard", "yard"),
    ("Woodworking", 'woodworking'),
    ("Metalworking", "metalworking"))


class Borrower(models.Model):
    def full_name_function(self):
        return "{} {}".format(self.first_name, self.last_name)

    user_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_created = models.DateField()
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
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
    user = models.ForeignKey(Borrower, null=True, blank=True)
    category = models.CharField(choices=category_list, null=True, blank=True, max_length=200)

    # slug = models.SlugField()
    # borrower = models.CharField(max_length=233, null=True, default=True)  # TODO: LINK TO USERS (see line below)
    #
    # # def createSlug(self):
    # #     self.slug = self.brand.lower() + "-" + self.model.lower() + "-" + self.tool_id
    # # slug = createSlug()
    #
    # def save(self, *args, **kwargs):
    #     self.string = slugify(str(self.tool_id) + self.brand)
    #     super(Tool, self).save(*args, **kwargs)
    #
    def __str__(self):
        return self.description


class Comment(models.Model):
    user = models.ForeignKey(Borrower)
    tool = models.ForeignKey(Tool)
    comment = models.TextField(max_length=288, blank=True, null=True)
    date = models.DateField()


class borrowingHistory(models.Model):
    user = models.ForeignKey(Borrower)
    tool = models.ForeignKey(Tool)
    date_checked_out = models.DateField()
    date_returned = models.DateField()
