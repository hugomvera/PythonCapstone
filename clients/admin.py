from django.contrib import admin
from .models import  Client
from .models import  Message

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ('code', 'description','time')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name','cellPhone','email','image_url')

admin.site.register(Client,ClientAdmin)
admin.site.register(Message,MessageAdmin)
