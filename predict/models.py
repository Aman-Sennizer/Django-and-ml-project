from django.db import models
import datetime


class PredictionResults(models.Model):
    user = models.CharField(max_length=30)
    cough = models.CharField(max_length=30)
    fever = models.CharField(max_length=30)
    sore_throat = models.CharField(max_length=30)
    breathing = models.CharField(max_length=30)
    classification = models.CharField(max_length=30)
    date = models.DateTimeField(default=datetime.datetime.now, blank=True)

    def __str__(self):
        return self.classification

