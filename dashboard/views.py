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

    
    # info_arr=list(info.values())
    

    if request.method == "POST":
        data = json.loads(request.body)
        name_slug = data['name']
        print(name_slug)
        # print(request.user.dashboard_setup)
        try:
            u = Dashboard.objects.get(user=request.user)

            u.pos.append(name_slug)
            u.save()
        except Dashboard.DoesNotExist:
            # user = User.objects.get(pk=request.user.id)
            Dashboard.objects.create(
                user=request.user,
                pos = [name_slug]
            )

        return render(request, "dashboard/index.html")

    try:
        checkDashboard = Dashboard.objects.get(user=request.user)
        pos = checkDashboard.pos
        dashboard = []
        for element in pos:
            URL=f"https://api.alternative.me/v2/ticker/{element}/"
            info = requests.get(URL).json()
            info_dict = info['data']
            info_arr = list(info_dict.values())
            dashboard.append({
                "name" : info_arr[0]['name'],
                "symbol" : info_arr[0]['symbol'],
                "price" : info_arr[0]['quotes']['USD']['price'],
                "change1" : info_arr[0]['quotes']['USD']['percent_change_1h'],
                "change24" : info_arr[0]['quotes']['USD']['percent_change_24h']
            })
    except Dashboard.DoesNotExist:
        dashboard = None
    

    cryptocurrencies = Cryptocurrency.objects.filter(user_id=request.user.id)
    

    context = {"cryptocurrencies" : cryptocurrencies, "dashboard" : dashboard}
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
    