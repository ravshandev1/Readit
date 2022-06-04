from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag


class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='articles')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    author_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='authors')
    author_comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='comments')
    website = models.URLField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
