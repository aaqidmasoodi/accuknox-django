from django.contrib import admin

from .models import Order, SignalLog

admin.site.register(Order)
admin.site.register(SignalLog)
