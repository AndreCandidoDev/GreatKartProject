from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from store import urls as store_urls
from carts import urls as carts_urls
from accounts import urls as accounts_urls
from orders import urls as orders_urls

urlpatterns = [
    path('orders/', include(orders_urls)),
    path('cart/', include(carts_urls)),
    path('store/', include(store_urls)),
    path('accounts/', include(accounts_urls)),
    path('securelogin/', admin.site.urls),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('', views.home, name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
