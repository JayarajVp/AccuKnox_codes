import threading
from django.core.signals import request_finished

def my_signal_handler(sender, **kwargs):
    print(f"Signal thread: {threading.get_ident()}")

request_finished.connect(my_signal_handler)

print(f"Main thread: {threading.get_ident()}")
request_finished.send(sender=None)
