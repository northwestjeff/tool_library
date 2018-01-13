from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator


def validateToolId(value):
    if len(value) != 5:
        raise ValidationError(
            _('Tool IDs must be exactly 5 numbers')
        )


class Tool(models.Model):
    tool_id = models.IntegerField(unique=True, validators=[MaxLengthValidator(5), MinLengthValidator(5)])  # TODO need to keep this to five numbers
    description = models.CharField(max_length=144)
    parts = models.CharField(max_length=144)
    brand = models.CharField(max_length=144)
    model = models.CharField(max_length=144)
    available = models.BooleanField(default=True)
    # slug = models.SlugField()
    # # borrower = models.CharField(max_length=233, null=True, default=True)  # TODO: LINK TO USERS (see line below)
    # # borrower = models.ForeignKey(User, null=True, blank=True)
    #
    # # def createSlug(self):
    # #     self.slug = self.brand.lower() + "-" + self.model.lower() + "-" + self.tool_id
    # # slug = createSlug()
    #
    # def save(self, *args, **kwargs):
    #     self.string = slugify(str(self.tool_id) + self.brand)
    #     super(Tool, self).save(*args, **kwargs)
    #
    # def __str__(self):
    #     return self.description


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
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip = models.CharField(max_length=5)
    late_tools = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name


class Comment(models.Model):
    
