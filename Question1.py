#models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

class MyModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
      
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler started.")
    time.sleep(5)  
    print("Signal handler finished.")


#views.py
from django.shortcuts import render
from .models import MyModel

def my_view(request):
    print("View execution started.")
    instance = MyModel.objects.create(name='Test Signal')
    print("View execution finished.")
    return render(request, 'my_template.html')

