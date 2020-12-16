from django.db import models
from config.storage_backends import SchemaStorage


class RootDocument(models.Model):
    file_name = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()


class SchemaDocument(models.Model):
    file_name = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(storage=SchemaStorage())
