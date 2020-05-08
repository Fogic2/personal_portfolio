from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    show1 = models.ImageField(upload_to='portfolio/images/')
    show2 = models.ImageField(upload_to='portfolio/images/')


    def __str__(self):
        return self.title
