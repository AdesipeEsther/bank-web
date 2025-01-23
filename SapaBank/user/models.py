from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
import time
from PIL import Image

# def profile_directory_path(instance, filename):
#     return f'images/{instance}/'

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='profiles/', default="default_image.jpg") #Install Pillow and google how to setup a default
    account_no = models.CharField(max_length=10, unique=True)
    account_balance = models.IntegerField(default=0)
    age = models.IntegerField(default=18)
    phone = models.CharField(max_length=15, blank=True, null=True)
    NIN = models.CharField(default = 0, max_length=20, blank=True, null=True)
    def image_tag(self):
        return mark_safe('<img src="{}" width="100" height="100">'.format(self.profile_pic.url))

    def __str__(self):
        return f"{self.user}"

class Transaction(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=0)
    sender = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="sender")
    receiver = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="receiver")

    def __str__(self):
        return f"{self.sender.user.username} sending ₦{self.amount} to {self.receiver.user.username}"