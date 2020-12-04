
from rest_framework import serializers
from .models import Subscription


class Subscriptionserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscription
        fields = ["subscription_id",
                    "kakaoemail",
                    "address",
                    "continuemonth"]
