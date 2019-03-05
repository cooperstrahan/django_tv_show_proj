from __future__ import unicode_literals
from django.db import models
import datetime

class ShowManager(models.Manager):
    def basic_validation(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title']="Title should be at least 2 characters"
        if len(postData['net']) < 3:
            errors['net']="Network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors['desc']="Description should be at least 10 characters"
        if postData['date'] == None:
            errors['date']="Form requires a release on or before today's date"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
