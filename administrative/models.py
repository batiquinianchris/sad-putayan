from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=120, verbose_name= 'First Name')
    last_name = models.CharField(max_length=120, verbose_name= 'Last Name')
    type = models.CharField(max_length=50, verbose_name= 'Type')
    status = models.IntegerField(verbose_name= 'Status')
    username = models.CharField(max_length=20, verbose_name= 'Username')
    password = models.CharField(max_length=30, verbose_name= 'Password')

    def __str__(self):
        return self.last_name + ", " + self.first_name

    """def get_absolute_url(self):
        return reverse("edit", kwargs={"id": self.id})"""

