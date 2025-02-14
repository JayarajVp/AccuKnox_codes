from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Global variable to store the atomic state inside the signal
signal_atomic_state = None

@receiver(post_save, sender=User)
def my_signal(sender, instance, **kwargs):
    global signal_atomic_state
    signal_atomic_state = transaction.get_connection().in_atomic_block
    print("Signal in transaction:", signal_atomic_state)

with transaction.atomic():
    User.objects.create(username="7testuser")
    caller_atomic_state = transaction.get_connection().in_atomic_block
    print("Caller in transaction:", caller_atomic_state)

# Compare values
print("Did signal run inside the same transaction?", signal_atomic_state == caller_atomic_state)
