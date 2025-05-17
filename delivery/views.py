import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from cart.cart import Cart
from django.http import JsonResponse
from .models import Order

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
# Отображение HTML формы
def delivery_form(request):
    cart = Cart(request)  # получаем корзину
    total_price = cart.get_total_price()  # итоговая сумма

    return render(request, 'delivery_form.html', {
        'total_price': round(total_price, 2)  # передаём в шаблон
    })




def submit_order(request):
    import json
    data = json.loads(request.body)

    city_ref = data.get('city')
    city_description = ''
    warehouse_description = data.get('warehouse', '')

    # Если доставка Новой Поштой — получаем название города
    if data.get('delivery_method') == 'np' and city_ref:
        # Опционально можно кэшировать, чтобы не делать много запросов
        city_description = get_city_description(city_ref)

    order = Order.objects.create(
        full_name=data['full_name'],
        phone_number=data['phone_number'],
        email=data['email'],
        delivery_method=data['delivery_method'],
        city_ref=city_ref,
        city_description=city_description,
        warehouse_description=warehouse_description,
        total_price=data['total_price']
    )
    return JsonResponse({'success': True})


def get_city_description(ref):
    url = 'https://api.novaposhta.ua/v2.0/json/'
    payload = {
        "apiKey": "ВАШ_API_КЛЮЧ",
        "modelName": "Address",
        "calledMethod": "getCities",
        "methodProperties": {"Ref": ref}
    }
    response = requests.post(url, json=payload)
    data = response.json()
    if data['success'] and data['data']:
        return data['data'][0]['Description']
    return ''