
from rest_framework import serializers
from .models import review


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = review
        fields = ["review_id",
                 "liquornumber",
                 "kakaoemail",
                 "score",
                 "created_at",
                 "updated_at",
                 "content"]