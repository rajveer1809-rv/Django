"""
Models for the services app.
"""

from django.db import models


class Service(models.Model):
    """
    Model representing a service.
    """

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    categoryName = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name
