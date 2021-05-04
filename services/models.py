from django.db import models
from django.urls import reverse


class Service(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()


    def get_absolute_url(self):
        return reverse("services-detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title