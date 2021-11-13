from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(ExtendedUser)
admin.site.register(Location)
admin.site.register(Node)
admin.site.register(UserLocation)
admin.site.register(Review)
admin.site.register(Document)
admin.site.register(Price)
admin.site.register(Action)
admin.site.register(Status)
admin.site.register(OrderStatusMap)
admin.site.register(Order)
admin.site.register(Device)
admin.site.register(OrderDevice)
