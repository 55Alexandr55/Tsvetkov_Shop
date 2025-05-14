from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Order
from .novaposhta import create_np_ttn

def create_order(request):
    if request.method == 'POST':
        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")
        city_ref = request.POST.get("city_ref")
        warehouse_ref = request.POST.get("warehouse_ref")
        total_price = request.POST.get("total_price")

        order = Order.objects.create(
            full_name=full_name,
            phone=phone,
            city_ref=city_ref,
            warehouse_ref=warehouse_ref,
            total_price=total_price
        )

        # Створюю ТТН
        ttn = create_np_ttn(order)
        if ttn:
            order.ttn = ttn
            order.save()

        return render(request, "thank_you.html", {"ttn": ttn})

    return render(request, "order_form.html")

