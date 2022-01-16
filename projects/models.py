from django.db import models

# Create your models here.
class Project(models.Model): 
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.CharField(max_length=100)
    cartegory = models.CharField(max_length=20, default="featured")
    featured = models.BooleanField(default="True")
    link = models.CharField(max_length=100, default="/")

    def __str__(self):
        return self.title