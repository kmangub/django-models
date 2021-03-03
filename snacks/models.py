from django.db import models
from django.contrib.auth import get_user_model

class Snack(models.Model):
    name = models.CharField(max_length=256)
    # LAB STUFF name = models.CharField(max_length=64)
    # LAB STUFF purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    purchaser = models.IntegerField(default=10)
    description = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name