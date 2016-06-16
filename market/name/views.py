from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

class BiddingView(TemplateView):
    template_name = 'bidding.html'
