from django.db import models
from django.db.models import Model
from django.contrib.auth import get_user_model
from . managers import ActiveLinkManager


# Create your models here.

class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(blank = True, unique = True)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
        )
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    objects = models.Manager()
    public = ActiveLinkManager()


def __str__(self):
    return (self.target_url)