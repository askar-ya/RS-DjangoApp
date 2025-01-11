from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField('Дата покупки', default=datetime.now)

    class Meta:
        db_table = 'subscription'

    def __str__(self):
        return self.user.username
