# utility functions used throughout the app

from core.const import DISTANCE_FEE_DICT, DISTANCE_FEE_BEYOND_THRESHOLD

def calculate_item_total(order_items):
    """
    function calculates the amount for each item and then returns the total amount for all items.
    """
    item_total = 0

    for order in order_items:
        item_total += order.get('price') * order.get('quantity')

    return item_total


def calculate_delivery_fee(distance):
    """
    function checks for distance from distance_fee_dict (Ordered Dict) and returns distance_fee accordingly.
    it will return DISTANCE_FEE_BEYOND_THRESHOLD
    """
    for key,val in DISTANCE_FEE_DICT.items():
        if distance <= key:
            return val

    return DISTANCE_FEE_BEYOND_THRESHOLD


def calculate_discount(offer, delivery_fee):
    """
    function calculates the discount depending on the 'offer_type'.
    """
    if offer.get('offer_type') == 'FLAT':
        discount = offer.get('offer_val')
    elif offer.get('offer_type') == 'DELIVERY':
        discount = delivery_fee
    else:
        discount = 0

    return discount