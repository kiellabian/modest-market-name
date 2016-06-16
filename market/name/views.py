from django.views.generic import TemplateView

from .models import BiddingEvent


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['events'] = BiddingEvent.objects.all()
        return context


class BiddingView(TemplateView):
    template_name = 'bidding.html'
