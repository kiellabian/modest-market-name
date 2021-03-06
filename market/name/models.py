from django.db import models
from django.utils.timezone import timedelta
from django.contrib.auth.models import User


class Name(models.Model):
    owner = models.ForeignKey(User, related_name='names')
    name = models.TextField(blank=False)

    @property
    def latest_event(self):
        return self.events.order_by('-started').first()

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'name'


class BiddingEvent(models.Model):
    name = models.ForeignKey(Name, related_name='events')
    started = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(default=timedelta(hours=1))
    starting_bid = models.FloatField(default=1.0)

    @property
    def highest_bid(self):
        if self.bids.count() == 0:
            return self.starting_bid
        else:
            return self.bids.order_by('-value').first().value

    def __unicode__(self):
        return self.name.name + ' event'

    class Meta:
        app_label = 'name'
        ordering = ['-pk']


class Bid(models.Model):
    owner = models.ForeignKey(User, related_name='bids')
    event = models.ForeignKey(BiddingEvent, related_name='bids')
    value = models.FloatField(default=0.0)

    class Meta:
        app_label = 'name'


class Balance(models.Model):
    owner = models.OneToOneField(User, related_name='balance')
    amount = models.FloatField(default=0.0)

    def __unicode__(self):
        return '{}\'s balance'.format(self.owner.username)

    class Meta:
        app_label = 'name'
