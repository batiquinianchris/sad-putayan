from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Section(models.Model):
    section_name = models.CharField(max_length=120, verbose_name= 'Section Name')
    status = models.IntegerField(verbose_name= 'Status')

    def __str__(self):
        return self.section_name

    def get_absolute_url(self):
        return reverse("edit", kwargs={"id": self.id})


