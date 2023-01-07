from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images/")
    preview = models.URLField(blank=True)
    github = models.URLField(blank=True)



    def __str__(self):
        return self.title