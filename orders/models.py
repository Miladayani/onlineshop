from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _

from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    is_paid = models.BooleanField(_('Is Paid?'), default=False)

    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=100)
    phone_number = PhoneNumberField(_('Phone Number'))
    address = models.CharField(_('Address'), max_length=700)

    order_note = models.TextField(_('Order Notes'), blank=True)

    zarinpal_authority = models.CharField(max_length=100, blank=True)
    zarinpal_ref_id = models.CharField(max_length=100, blank=True)
    zarinpal_data = models.TextField(blank=True)

    datetime_created = models.DateTimeField(_('Created'), auto_now_add=True, blank=True)
    datetime_modified = models.DateTimeField(_('Modified'), auto_now=True)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_price(self):
        return sum(item.quantity * item.price for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'OrderItem {self.id} or order {self.order.id}'
