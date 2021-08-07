import json

from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from core.util_func import calculate_item_total, calculate_delivery_fee, calculate_discount

# Create your views here.

@api_view(['GET'])
def home(request):
    return HttpResponse("This is a Demo Project | Server Running Perfectly ")


@api_view(['POST',])
def calculate_order_total(request):
    """
    Args:
        order_items : a JSON List (as provided in the document) having json objects with keys - name, quantity & price(in paise)
        distance : distance in metres
        offer: OPTIONAL
            JSON object having  offer_type ('FLAT', 'DELIVERY') and offer_val ( in paise )
    """
    try:
        order_items = request.data.get("order_items")
        distance = request.data.get("distance")
        offer = request.data.get("offer")

        if not order_items or not distance:
            res = {
                'Input Error' : 'Input must contain order_items and distance.'
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        item_total = calculate_item_total(json.loads(order_items))
        delivery_fee = calculate_delivery_fee(int(distance))

        order_total_without_offer = item_total + delivery_fee

        if offer:
            discount = min(calculate_discount(json.loads(offer), delivery_fee), order_total_without_offer)
        else:
            discount = 0

        total_order_cost = order_total_without_offer - discount

        res = {
            'order_total' : total_order_cost
        }

        return Response(res, status=status.HTTP_200_OK)

    except Exception as e:
        res = {
            "Exception" : str(e)
        }
        return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)