from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from .models import BiddingEvent
from .models import Name

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
        event = name.events.order_by('-started').first()
        highest_bid = event.bids.order_by('value').first()
        context['name'] = name.name
        context['starting'] = event.starting_bid
        context['highest_bid'] = highest_bid
        context['next_bid'] = highest_bid.value + 1
        context['past_bids'] = event.bids.order_by('value')[1:]
        return context
