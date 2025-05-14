from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    #для корзины покупок
    path('cart/', include('cart.urls', namespace='cart')),  #Если человек заходит по адресу /cart/ тогда ищи дальнейшие маршруты во вложенном файле cart/urls.py  и все маршруты будут начинаться с cart
    # логин, регистрация, выход с профиля
    path('users/', include('users.urls', namespace='users')),
    # каталог, страница продукта
    path('', include('main.urls', namespace='main')),
    #оформление доставки
    path('orders/', include('orders.urls', namespace='orders')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)