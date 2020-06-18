from django.db import models

# Create your models here.
class Projects(models.Model):
    title=models.CharField(max_length=250)
    thumbnails=models.FileField(upload_to='thumbnails')
    timestamp = models.DateTimeField(auto_now_add=True)
    link=models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Messages(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    subject=models.CharField(max_length=250)
    message=models.TextField()

    def __str__(self):
        return self.firstname
