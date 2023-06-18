from django.db import models


# Create your models here.
class Works(models.Model):
    style = models.CharField(max_length=50)
    resolution = models.IntegerField()
    author = models.CharField(max_length=50)
    software = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.style} - {self.resolution} - {self.author} - {self.software}"


class Trideshniki(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    experience = models.IntegerField()
    age = models.IntegerField()
    level = models.CharField(max_length=50)
    company = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.surname} - {self.experience} - {self.age} - {self.level} - {self.company}"
