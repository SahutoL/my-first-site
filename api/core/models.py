from django.db import models


class EconomicLessons(models.Model):
    title = models.CharField(max_length=120)
    info = models.CharField(max_length=50)
    detail = models.TextField()

    def __str_(self):
        return "{} について".format(self.title)
