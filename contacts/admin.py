from django.contrib import admin
from .models import  Contact
from .models import  Message

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ('code', 'description','time')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','cellPhone','email','image_url')

admin.site.register(Contact,ContactAdmin)
admin.site.register(Message,MessageAdmin)
