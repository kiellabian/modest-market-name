from django.contrib import admin

from .models import Name, BiddingEvent, Bid, Balance


admin.site.register(Name)
admin.site.register(BiddingEvent)
admin.site.register(Bid)
admin.site.register(Balance)
