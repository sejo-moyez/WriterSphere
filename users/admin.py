from django.contrib import admin
from .models import User, Writer, Fine

# Register your models here.

admin.site.register(User)
admin.site.register(Writer)
admin.site.register(Fine)

from .models import Order, Invoice, Report

# Register your models here.
admin.site.register(Order)
admin.site.register(Invoice)
admin.site.register(Report)

