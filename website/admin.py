from django.contrib import admin
from .models import User, Group, Event, UserAddon, AddonInstance, Addon, Attendee

# Register your models here.

admin.site.register(User)
admin.site.register(Group)
admin.site.register(Attendee)
admin.site.register(Event)
admin.site.register(UserAddon)
admin.site.register(AddonInstance)
admin.site.register(Addon)
