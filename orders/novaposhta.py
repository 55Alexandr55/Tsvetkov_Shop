
from dotenv import load_dotenv
import dotenv
import os


def create_np_ttn(order):
    url = "https://api.novaposhta.ua/v2.0/json/"
    headers = {"Content-Type": "application/json"}

    payload = {
        "apiKey": 'API_NOVAPOSHTA',
        "modelName": "InternetDocument",
        "calledMethod": "save",
        "methodProperties": {
            "NewAddress": "1",
            "PayerType": "Sender",
            "PaymentMethod": "Cash",
            "CargoType": "Cargo",
            "VolumeGeneral": "0.1",
            "Weight": "1",
            "ServiceType": "WarehouseWarehouse",
            "SeatsAmount": "1",
            "Description": "Гаджети та аксесуари",
            "Cost": 'total_price',
            "CitySender": "КОД_МІСТА_ВІДПРАВНИКА",
            "SenderAddress": "КОД_ВІДДІЛЕННЯ_ВІДПРАВНИКА",
            "Sender": "КОД_КОНТРАГЕНТА_ВІДПРАВНИКА",
            "ContactSender": "КОД_КОНТАКТУ_ВІДПРАВНИКА",
            "SendersPhone": "ТЕЛЕФОН_ВІДПРАВНИКА",
            "CityRecipient": order.city_ref,
            "RecipientAddress": order.warehouse_ref,
            "ContactRecipient": order.recipient_full_name,
            "RecipientsPhone": order.phone,
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    if data.get("success"):
        ttn = data["data"][0]["IntDocNumber"]
        return ttn
    else:
        print("Nova Poshta error:", data.get("errors"))
        return None
