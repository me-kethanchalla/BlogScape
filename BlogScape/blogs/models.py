from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class blog (models.Model) :
    title = models.CharField(max_length=100)
    content = models.TextField()
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.now)


    class Meta :
        ordering = ('-time', )

    def __str__ (self):
        return self.title

