from django.conf import settings

# Create your models here.
from django.db import models


class SearchModel(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    publish_date = models.DateTimeField(auto_now_add=True)
    query = models.CharField(max_length=120)
