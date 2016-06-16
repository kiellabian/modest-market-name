import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from .models import BiddingEvent, Name, Bid, Balance


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['events'] = BiddingEvent.objects.all()
        return context


class BiddingView(TemplateView):
    template_name = 'bidding.html'

    def get_context_data(self, **kwargs):
        context = {}
        name = get_object_or_404(Name, pk=kwargs['pk'])
        event = name.latest_event
        highest_bid = event.bids.order_by('-value').first()
        context['name'] = name
        context['starting'] = event.starting_bid
        context['highest_bid'] = highest_bid
        context['next_bid'] = event.highest_bid + 1
        context['past_bids'] = event.bids.order_by('-value')[1:]
        return context

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        value = float(self.request.POST.get('value'))
        user = self.request.user
        name = get_object_or_404(Name, pk=pk)
        event = name.latest_event
        msg = {}
        previous_bid = event.bids.order_by('-value').first()
        msg['previous_bid'] = {
            'name': previous_bid.owner.username,
            'value': '%.1f' % previous_bid.value,
        }
        new_bid = Bid.objects.create(owner=user, event=event, value=value)
        current_balance = user.balance.amount
        user.balance.amount = current_balance - value
        user.balance.save()

        msg['new_bid'] = {
            'name': new_bid.owner.username,
            'value': '%.1f' % new_bid.value,
        }

        return HttpResponse(json.dumps(msg))
