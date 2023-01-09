from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    link = models.URLField()
    date = models.DateField()


    def __str__(self):
        return self.title