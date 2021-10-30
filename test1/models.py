from django.db import models

# Create your models here.


class Book(models.Model):
    titleid = models.charfield(max_length=100, blank=true)
    authorid = models.charfield(max_length=100, blank=true)
    isbnid = models.charfield(max_length=100, blank=true)
    publisherid = models.charfield(max_length=100, blank=true)

    def _str_(self):
        return self.title
