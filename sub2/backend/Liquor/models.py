from django.db import models

# Create your models here.
# from Liquor import models
# from Liquor.serializer import Liquorserializer

class Liquor(models.Model):
    liquornumber = models.AutoField(primary_key=True)
    liquorname = models.CharField(max_length=50, null=False)
    liquorarea = models.CharField(max_length=50, null=False)
    liquorcategory = models.CharField(max_length=50, null=False)
    liquoralcohol = models.CharField(max_length=10, null=False)
    liquorprice = models.IntegerField(null=False)
    liquoringredient = models.CharField(default="", max_length=1000, null=True)
    sweet = models.IntegerField(default=0, null=False)
    sour = models.IntegerField(default=0, null=False)
    cloudy = models.IntegerField(default=0, null=False)
    carbonated = models.IntegerField(default=0, null=False)
    plain = models.IntegerField(default=0, null=False)
    body = models.IntegerField(default=0, null=False)
    bitter = models.IntegerField(default=0, null=False)
    fancy = models.IntegerField(default=0, null=False)
    spicy = models.IntegerField(default=0, null=False)
    salty = models.IntegerField(default=0, null=False)
    sourness = models.IntegerField(default=0, null=False)
    acerbity = models.IntegerField(default=0, null=False)
    flavor = models.IntegerField(default=0, null=False)
    url = models.CharField(max_length=3000 , default="https://www.daelim.ac.kr/coming_soon.jpg")

    class Meta:
        pass
