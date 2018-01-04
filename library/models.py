from django.db import models


class Tools(models.Model):
    tool_id = models.CharField(max_length=233)
    name = models.CharField(max_length=233)
    make = models.CharField(max_length=244)
    type = models.CharField(max_length=233)

    def __str__(self):
        return self.name

class Users(models.Model):
    user_id = models.CharField(max_length=233)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    full_name = "{} {}".format(first_name, last_name)

    def __str__(self):
        return self.full_name



