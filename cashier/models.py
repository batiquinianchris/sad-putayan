from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Fees_Accounts(models.Model):
    FA_name = models.CharField(max_length=120, verbose_name= 'Fee Name')
    amount = models.FloatField(verbose_name= 'Amount')

    def __str__(self):
        return self.FA_name

    def get_absolute_url(self):
        return reverse("edit", kwargs={"id": self.id})

