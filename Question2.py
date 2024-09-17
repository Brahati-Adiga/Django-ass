#models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading

class MyModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal in the thread {threading.current_thread().name}")

#views.py
from django.shortcuts import render
from .models import MyModel
import threading

def my_view(request):
    print(f"Signal in the thread {threading.current_thread().name}")
    instance = MyModel.objects.create(name='Test Signal')
    return render(request, 'my_template.html')
