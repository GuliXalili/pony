from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=255)
    surename = models.CharField(max_length=255)
    group = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
