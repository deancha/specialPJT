
from rest_framework import serializers
from .models import Order


class Orderserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ["order_id", "tid", "username", "kakaoemail", "liquornumber",
                  "liquorname", "liquorprice", "quantity", "address", "waynumber",
                  "phonenumber", "uniqueness",
                  "created_at", "status"]
