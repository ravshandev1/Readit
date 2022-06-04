from django.db import models


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='team')
    profession = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
