# supplier/models.py

from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    gst_no = models.CharField(max_length=15, unique=True)
    tds_applicable = models.BooleanField(default=False)
    contact = models.CharField(max_length=15, blank=True, null=True)  # Now optional
    email = models.EmailField(blank=True, null=True)  # Now optional

    def __str__(self):
        return self.name
