from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
    
class Schedule(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    date = models.DateTimeField( auto_now=False, auto_now_add=False)

    def _str_(self):
        return self.name