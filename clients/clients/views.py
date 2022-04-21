from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
from .models import Withdrawal
from .models import Deposit


# Create your views here.

# /clients  -> index
def index(request):
    # Contact.objects.filter()
    clients = Client.objects.all()
    withdrawals = Withdrawal.objects.all()
    deposits = Deposit.objects.all()
    # return HttpResponse('Hello World')

    #######################need to show the balance#########
    Balance = []
    for p in Client.objects.raw('SELECT * FROM clients_client'):
        sum = 0.0
        owed = 0.0
        balance = 0.0
        print("looking at " + p.name + " whose id is  " + p.applicationId)
        for d in Deposit.objects.raw('Select * from clients_deposit'):
            print('\t' + d.applicationId)
            if d.applicationId == p.applicationId:
                print("\t\t there is a match here")
                sum = float(d.transactionAmount) + sum
                print('\t\t updated the sum to ' + ' ' + str(sum) + ' for ' + d.applicationId)
        for w in Withdrawal.objects.raw('Select * from clients_withdrawal'):
            print("in withdrawal loop")
            print("\t the id is of withdrawal " + w.applicationId)
            if (w.applicationId == p.applicationId):
                print("there is a match here within the withdrawal")
                owed = float(w.transactionAmount) + owed
                print('\t\t\t updated the owed to ' + ' ' + str(owed) + ' for ' + w.applicationId)
        balance = str(sum - owed)
        print('#####################################')
        print('the balance for ' + p.name + ' is ' + str(balance) + " whose id is " + str(p.applicationId))
        Balance.append(str(balance))

    return render(request, 'index.html', {'clients': clients, 'withdrawals': withdrawals, 'deposits': deposits,'Balance':Balance})


def new(request):
    return HttpResponse('New Contacts')
