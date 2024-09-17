#models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler running")
    raise Exception("Signal handler failed")

#views.py
from django.shortcuts import render
from .models import MyModel
from django.db import transaction

def my_view(request):
    print("Signals started")
    try:
        with transaction.atomic():
            instance = MyModel.objects.create(name='Test')
    except Exception as e:
        print(f"Exception caught {e} \n")
    return render(request, 'index.html')
    
