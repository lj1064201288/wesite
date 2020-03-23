from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Poll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='话题')
    created_at = models.DateTimeField(auto_now_add=True)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class PollItem(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    vote = models.PositiveIntegerField(default=0)
    images_url = models.ImageField(blank=True, upload_to='pollitem/static/user_images')

class VoteCheck(models.Model):
    userid = models.PositiveIntegerField()
    pollid = models.PositiveIntegerField()
    vote_time = models.DateField()
