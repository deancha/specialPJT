from rest_framework import serializers
from .models import Cart


class Cartserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ["cart_id","kakaoemail", "liquornumber", "liquorname", "liquorprice", "quantity", "url"]
