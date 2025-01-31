from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    imageLink = models.TextField()
    visible = models.BooleanField(default=True)

    def _str_(self):
        return self.title