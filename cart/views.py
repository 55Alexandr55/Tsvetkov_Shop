from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from django.views import View
from main.models import Item



def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

def cart_add(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)

    cart.add(item)
    return redirect('cart:cart_detail')


def cart_remove(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)
    return redirect('cart:cart_detail')


class CartUpdateView(View):
    def post(self, request, item_id):
        cart = Cart(request)
        quantity = request.POST.get('quantity', 1)
        try:
            quantity = int(quantity)
            if quantity < 1:
                quantity = 1
        except ValueError:
            quantity = 1
        item = get_object_or_404(Item, id=item_id)

        if quantity > 0:
            cart.add(item, quantity, update_quantity=True)
        else:
            cart.remove(item)

        return redirect('cart:cart_detail')


