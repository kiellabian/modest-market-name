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
        context['name'] = name.name
        return context
