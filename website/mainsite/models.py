from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from logininfo.models import CustomUser

# Create your models here.

@python_2_unicode_compatible
class Poll(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)
    created_date = models.DateField(auto_now_add=True)
    enaled = models.BooleanField(default=True)

    def __str__(self):
        return self.name



@python_2_unicode_compatible
class PollItem(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)
    image_url = models.CharField(max_length=500, null=True, blank=True)
    vote = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name

class VoteCheck(models.Model):
    userid = models.PositiveIntegerField()
    pollid = models.PositiveIntegerField()
    vote_date = models.DateField()
