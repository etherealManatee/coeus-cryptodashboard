from django.shortcuts import render, redirect
from dashboard.models import *
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
@csrf_exempt
@login_required
def dashboard_view(request):

    # d = Dashboard.objects.create(user=request.user, pos=["bitcoin", 1])
    # print(request.user.dashboard_setup.pos)

    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        
        # search = request.POST['q']
        # URL = f"https://api.alternative.me/v2/ticker/{search}/"
        # page = requests.get(URL)
        # print(page.text)
        # page_json = page.json()['data']
        # print(type(page_json))
        # the_dict = json.loads(page.json())

        # print(page_json)
        # if len(page_json) > 0:
        #     print('more than 0')
        #     # first_key = list(page_json['data'].keys())[0]
        #     # print(first_key)
        #     # name = page_json['data'].first_key.name
        #     # print(name)
        #     return redirect(request, "dashboard/index.html")
        # else:
        #     print('there is nothing, error')
        #     return redirect(request, "dashboard/index.html")

        return render(request, "dashboard/index.html")

    cryptocurrencies = Cryptocurrency.objects.filter(user_id=request.user.id)
    

    context = {"cryptocurrencies" : cryptocurrencies}
    return render(request, "dashboard/index.html", context)

@csrf_exempt
@login_required

def add_crypto(request, crypto_name):
    if request.method == "POST":
        data = json.loads(request.body)
        first_dict = data.get('data')
        first_arr = list(first_dict.values())
        id_of_crypto_from_api = first_arr[0]['id']
        symbol_of_crypto_from_api = first_arr[0]['symbol']
        user_id = request.user.id

        user = User.objects.get(pk=user_id)
        user.cryptocurrencies.create(
            name=crypto_name,
            api_id=id_of_crypto_from_api,
            symbol=symbol_of_crypto_from_api
        )

        return render(request, "dashboard/base.html")
    
    # cryptocurrencies = Cryptocurrency.objects.get(user_id=request.user.id)
    # print(cryptocurrencies)
    
    return render(request, "dashboard/base.html")
    