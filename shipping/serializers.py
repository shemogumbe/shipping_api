from rest_framework import serializers

from models import Shipment, Shipping

class ShippingSerializer(serializers.modelserilizer):
    class Meta:
        model = Shipping
        fields = ('id', 'shipping_first_name', 'shipping_last_name',
            'shipping_address_line1', 'shipping_address_line2',
            'shipping_city', 'shipping_state', 'shipping_country',
            'shipping_phone_number')

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ('id', 'retailer', 'product_id','shipping',
            'quatity')