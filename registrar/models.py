from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class SHS_Subjects(models.Model):
    SHS_subjectName = models.CharField(max_length=120, verbose_name= 'Subject Name')
    SHS_desc = models.CharField(max_length=12, verbose_name= 'Description')
    SHS_trackStatus = models.IntegerField()

    def __str__(self):
        return self.SHS_desc

    def get_absolute_url(self):
        return reverse("edit", kwargs={"id": self.id})

