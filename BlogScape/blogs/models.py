from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class blog (models.Model) :
    title = models.CharField(max_length=100)
    content = models.TextField()
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.now)

    #for newest blogs appearing first
    class Meta :
        ordering = ('-time', )

    def __str__ (self):
        return self.title


class comments ( models.Model ) :
    blog = models.ForeignKey(blog, on_delete=models.CASCADE, related_name="comments")
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    Add_Comment = models.TextField()
    time = models.DateTimeField(default=datetime.now)

    #for newest blogs appearing first
    class Meta :
        ordering = ('-time', )

    #not needed, but when i do print(comment) for any object in this class, then it prints this
    def __str__ (self):
        return self.Add_Comment



