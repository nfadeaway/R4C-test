from django.db.models.signals import post_save
from django.dispatch import receiver

from customers.models import Customer
from orders.models import Order
from robots.models import Robot
from services import send_order_notification


@receiver(post_save, sender=Robot)
def send_order_email(instance, **kwargs):
    orders = Order.objects.filter(robot_serial=instance.serial)
    if orders:
        for order in orders:
            customer_email = Customer.objects.get(id=order.customer_id).email
            send_order_notification(customer_email, instance.serial)
