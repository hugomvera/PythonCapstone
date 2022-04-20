from django.contrib import admin
from .models import Client
from .models import Message
from .models import Deposit
from .models import Withdrawal

# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'time')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'cellPhone', 'email', 'image_url')


class DepositAdmin(admin.ModelAdmin):
    list_display = ('depositID', 'applicationId', 'transactionAmount', 'transactionStatus',
                    'transactionDate', 'datetime', 'transactionType', 'currencyCode')


admin.site.register(Client, ClientAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Deposit, DepositAdmin)


# for withdrawals
class WithdrawalAdmin(admin.ModelAdmin):
    list_display = ('withdrawalID', 'applicationId', 'transactionAmount', 'transactionStatus',
                    'transactionDate', 'datetime', 'transactionType', 'currencyCode')


admin.site.register(Withdrawal, WithdrawalAdmin)
