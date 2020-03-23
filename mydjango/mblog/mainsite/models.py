from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    abstract = models.CharField(max_length=120, blank=True)
    pub_date = models.DateTimeField(auto_now_add=timezone.now)
    class Mate:
        ordering = ('-pub_date', )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.abstract = self.body[:100] + '...'
        return super(Post, self).save(*args, **kwargs)