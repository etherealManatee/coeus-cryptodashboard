from django.shortcuts import render
from dashboard.models import *
import requests

# Create your views here.
def dashboard_view(request):

    instrument = Instruments.objects.all()
    BTC_URL = instrument[1].source
    ETH_URL = instrument[2].source
    ADA_URL = instrument[3].source
    btc = requests.get(BTC_URL)
    eth = requests.get(ETH_URL)
    ada = requests.get(ADA_URL)


    context = {"btc" : btc.json(), "eth" : eth.json(), "ada" : ada.json()}
    return render(request, "dashboard/index.html", context)