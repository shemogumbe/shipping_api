
from django.conf.urls import url
from django.contrib import admin

from shipping.views import add_shipment

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'shipment', add_shipment)
]
