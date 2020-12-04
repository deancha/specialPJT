from django.db import models

# Create your models here.


class Subscription(models.Model):

    subscription_id = models.AutoField(primary_key=True)
    kakaoemail = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    continuemonth = models.IntegerField(default=1, null=False)
    created_at = models.DateField(auto_now=True)
    next_payday = models.DateField(auto_now=True)
