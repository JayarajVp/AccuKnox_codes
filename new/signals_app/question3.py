from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal(sender, instance, **kwargs):
    print("Signal in transaction:", transaction.get_connection().in_atomic_block)

with transaction.atomic():
    User.objects.create(username="4testuser")
    print("Caller in transaction:", transaction.get_connection().in_atomic_block)
