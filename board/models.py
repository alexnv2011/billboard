from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    time_create = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.caption[:125] + '.... | ' + self.preview

    @property
    def preview(self):
        return self.text[:125] + "..."


class Reply(models.Model):
    text = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:125] + '...'


