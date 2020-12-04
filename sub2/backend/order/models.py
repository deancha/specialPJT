from django.db import models

# Create your models here.


class Order(models.Model):
    class Meta:
        pass
    order_id = models.AutoField(primary_key=True)
    tid = models.CharField(max_length=100, null=False)
    username = models.CharField(max_length=10, null=False)
    kakaoemail = models.CharField(max_length=100, null=False)
    liquornumber = models.IntegerField(null=False)
    liquorname = models.CharField(max_length=100, null=False)
    liquorprice = models.IntegerField(default=1, null=False)
    quantity = models.IntegerField(null=False)
    address = models.CharField(max_length=100, null=False)
    phonenumber = models.CharField(max_length=100, null=False)
    waynumber = models.CharField(max_length=80, null=False, default="-")
    uniqueness = models.CharField(max_length=500, null=False)
    created_at = models.DateTimeField(auto_now=False)
    status = models.CharField(max_length=30, default="배송전")
