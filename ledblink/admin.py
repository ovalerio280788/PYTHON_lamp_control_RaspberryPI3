from django.contrib import admin
from .models import ControlLamp


class ledBlinkAdmin(admin.ModelAdmin):
    list_display = ['state']


admin.site.register(ControlLamp, ledBlinkAdmin)
