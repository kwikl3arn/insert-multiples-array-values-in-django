from django.db import models


class test(models.Model):
    name = models.TextField()
    mail = models.EmailField(blank=True)
    mobile = models.CharField(max_length=10, blank=True)
    date = models.TimeField(auto_now_add=True)
