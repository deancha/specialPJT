from django.db import models

class review(models.Model):
    objects = models.Manager()
    review_id  = models.AutoField(primary_key=True)
    liquornumber = models.IntegerField(null=False)
    kakaoemail = models.CharField(max_length=100, null=False)
    score = models.FloatField(default=0, null=False)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    content	= models.CharField(max_length=300, null=False)

