from django.contrib import admin

from .models import QRCode, QrZone, Feedback


class serviceAdmin(admin.ModelAdmin):
    list_display = ['contact', 'name', 'text']


class ZoneAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(QrZone,ZoneAdmin)
admin.site.register(Feedback, serviceAdmin)
admin.site.register(QRCode)
# Register your models here.
