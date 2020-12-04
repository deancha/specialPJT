
from rest_framework import serializers
from .models import Liquor


class Liquorserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Liquor
        fields = ["liquornumber", "liquorname", "liquorarea", "liquorcategory", "liquorarea", "liquoralcohol", "liquorprice", "liquoringredient",
                  "sweet", "sour", "cloudy", "carbonated", "plain", "body", "bitter", "fancy", "spicy", "salty", "sourness", "acerbity", "flavor","url"]
