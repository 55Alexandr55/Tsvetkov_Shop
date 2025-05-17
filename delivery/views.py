
import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json



API_KEY = 'c00003091e94a54b172d290a403d9cbf'

# Получение городов
@csrf_exempt
def get_np_cities(request):
    url = 'https://api.novaposhta.ua/v2.0/json/'
    payload = {
        "apiKey": API_KEY,
        "modelName": "Address",
        "calledMethod": "getCities",
        "methodProperties": {}
    }
    response = requests.post(url, json=payload)
    #print(response.json())
    return JsonResponse(response.json())

# Получение отделений по городу
@csrf_exempt
def get_np_warehouses(request):
    #data = json.loads(request.body)
    city_ref = request.GET.get("cityRef")
    url = 'https://api.novaposhta.ua/v2.0/json/'
    payload = {
        "apiKey": API_KEY,
        "modelName": "Address",
        "calledMethod": "getWarehouses",
        "methodProperties": {
            "CityRef": city_ref
        }
    }
    response = requests.post(url, json=payload)
    return JsonResponse(response.json())

# Отображение HTML формы
def delivery_form(request):
    return render(request, 'delivery_form.html')



''' Создание ТТН (накладной) ТОПОМ
@csrf_exempt
def create_ttn(request):
    data = json.loads(request.body)
    url = 'https://api.novaposhta.ua/v2.0/json/'
    payload = {
        "apiKey": API_KEY,
        "modelName": "InternetDocument",
        "calledMethod": "save",
        "methodProperties": {
            "PayerType": "Sender",
            "PaymentMethod": "Cash",
            "CargoType": "Parcel",
            "VolumeGeneral": "0.1",
            "Weight": "1",
            "ServiceType": "WarehouseWarehouse",
            "SeatsAmount": "1",
            "Description": data.get("description"),
            "Cost": data.get("cost"),
            "CitySender": data.get("citySender"),
            "SenderAddress": data.get("senderAddress"),
            "ContactSender": data.get("contactSender"),
            "SendersPhone": data.get("senderPhone"),
            "CityRecipient": data.get("cityRecipient"),
            "RecipientAddress": data.get("recipientAddress"),
            "ContactRecipient": data.get("contactRecipient"),
            "RecipientsPhone": data.get("recipientPhone")
        }
    }
    response = requests.post(url, json=payload)
    return JsonResponse(response.json())

# Отслеживание статуса посылки
@csrf_exempt
def track_ttn(request):
    data = json.loads(request.body)
    ttn = data.get("ttn")
    url = 'https://api.novaposhta.ua/v2.0/json/'
    payload = {
        "apiKey": API_KEY,
        "modelName": "TrackingDocument",
        "calledMethod": "getStatusDocuments",
        "methodProperties": {
            "Documents": [
                {"DocumentNumber": ttn}
            ]
        }
    }
    response = requests.post(url, json=payload)
    return JsonResponse(response.json())
'''
