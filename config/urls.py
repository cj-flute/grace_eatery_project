from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('menu/', include('menu.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('addresses/', include('addresses.urls')),
    path('dashboard/', include('dashboard.urls')),
]
