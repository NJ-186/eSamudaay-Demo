from django.db import models

from django.utils.translation import gettext_lazy as _

# Create your models here.

# A model created to just dump the requests that we get. Could add this functionality. Not using this in the current version.

# class Order(models.Model):
#     order_items = models.TextField(
#         help_text=_(
#             'list of items ordered. Each item will have a name(string), quantity(int), price(int) in paisa.'
#         )
#     )
#     distance = models.IntegerField(
#         help_text=_(
#             'delivery distance in meters. Allowed values for distance are integers between 0 and 500000 (both inclusive.'
#         )
#     )
#     offer = models.TextField(
#         null=True,
#         blank=True,
#         help_text=_(
#             'information about the offer applied to the order.'
#         )
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     response = models.TextField(
#         null=True,
#         blank=True,
#         help_text=_(
#             'order_total provided after calculating.'
#         )
#     )

#     class Meta:
#         verbose_name = 'order'
#         verbose_name_plural = 'orders'
#         db_table = 'order'
