from django.conf import settings
from main.models import Item

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    #def add (self, item, quantity=1):
     #   item_id= str(item.id)
      #  if item_id not in self.cart:
       #     self.cart[item_id] = {"quantity": 0 }
        #self.cart[item_id]["quantity"] += quantity
        #self.save()

    def add(self, item, quantity=1, update_quantity=False):
        item_id = str(item.id)
        if item_id not in self.cart:
            self.cart[item_id] = {'quantity': 0}
        if update_quantity:
            self.cart[item_id]['quantity'] = quantity  # перезаписываем
        else:
            self.cart[item_id]['quantity'] += quantity  # прибавляем
        self.save()




    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, item):
        item_id= str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def get_total_price(self):
        total = 0
        for item_id,item_date in self.cart.items():
            try:
                item = Item.objects.get(id=item_id)
                total += item.get_price_with_discount() * item_date["quantity"]
            except Item.DoesNotExist:
                continue
        return total



    def __iter__(self):
        item_ids = self.cart.keys()
        items = Item.objects.filter(id__in=item_ids)
        for item in items:
            total_price = item.get_price_with_discount()     #Что было:в 14.59 ! 10.05.25    total_price = self.get_price_with_discount()
            quantity = self.cart[str(item.id)]["quantity"]
            yield {
                'item': item,
                'quantity': quantity,
                'total_price': total_price * quantity,
            }




    def __len__ (self):

        return sum(item['quantity'] for item in self.cart.values() )

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True