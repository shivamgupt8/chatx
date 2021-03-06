from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    images = models.ImageField(upload_to='media', blank=True)

    def get_absolute_url(self):
        return reverse('home-detailpost', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-date_posted']


class Message(models.Model):
    From = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    To = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.From


class Group(models.Model):
    gname = models.CharField(max_length=100)
    gusers = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.gname

    # def get_absolute_url(self):
    #     return reverse("Comments_detail", kwargs={"pk": self.pk})


class GroupMessage(models.Model):
    gname = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.gname

    def get_absolute_url(self):
        return reverse("Comments_detail", kwargs={"pk": self.pk})
