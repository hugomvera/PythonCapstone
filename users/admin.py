from django.contrib import admin
from .models import Player

# Register your models here.


class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "piece", "balance")


admin.site.register(Player, PlayerAdmin)
