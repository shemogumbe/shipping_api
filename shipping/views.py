from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from models import Shipping, Shipment
from serializers import ShipmentSerializer, ShippingSerializer

@api_view(['POST'])
@renderer_classes((JSONRenderer, ))
def add_shipment(request):
    data = request.data
    shipment = {
    'retailer': data['retailer'],
    'product_id': data['product_id'],
    'quantity': data['quantity']
    }
    shipping = data['shipping']
    shipment_serializer = ShipmentSerializer(data=shipment)
    if shipment_serializer.is_valid():
        shipment_serializer.save()

    shipping_serializer = ShippingSerializer(data=shipping)
    if shipping_serializer.is_valid():
        shipping_serializer.save()
    else:
        print shipping_serializer.errors

    message = {'success': "Shipping added successfully"}
    return Response(message)
