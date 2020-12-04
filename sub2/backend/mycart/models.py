from django.db import models

# Create your models here.


class Cart(models.Model):
    class Meta:
        pass
    cart_id = models.AutoField(primary_key=True)
    kakaoemail = models.CharField(max_length=50, null=False)
    liquornumber = models.IntegerField(null=False)
    liquorname = models.CharField(max_length=100, null=False)
    liquorprice = models.IntegerField(default=1, null=False)
    quantity = models.IntegerField(null=False)
    url = models.CharField(
        max_length=3000, default="https://www.daelim.ac.kr/coming_soon.jpg")
