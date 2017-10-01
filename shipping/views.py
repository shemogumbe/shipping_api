from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from models import Shipping, Shipment

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

    shipment_record = Shipment(**shipment)
    shipment_record.save()
    shipping_record = Shipping(**shipping)
    shipping_record.save()

    message = {'success': "Shipping added successfully"}
    return Response(message)
