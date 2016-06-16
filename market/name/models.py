from django.db import models
from django.utils.timezone import timedelta
from django.contrib.auth.models import User


class Name(models.Model):
    owner = models.ForeignKey(User, related_name='names')
    name = models.TextField(blank=False)


class BiddingEvent(models.Model):
    name = models.ForeignKey(Name, related_name='events')
    started = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(default=timedelta(hours=1))


class Bid(models.Model):
    owner = models.ForeignKey(User, related_name='bids')
    event = models.ForeignKey(BiddingEvent, related_name='bids')
    value = models.FloatField(default=0.0)
