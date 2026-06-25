from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #     path('apps/accounts/', include('accounts.urls')),
    #     path('apps/menu/', include('menu.urls')),
    #     path('apps/cart/', include('cart.urls')),
    #     path('apps/orders/', include('orders.urls')),
    #     path('apps/addresses/', include('addresses.urls')),
    #     path('apps/dashboard/', include('dashboard.urls')),
]
