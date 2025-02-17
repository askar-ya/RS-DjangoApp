from django.db import models
from accounts.models import User
from datetime import datetime


# Create your models here.
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField('Дата покупки', default=datetime.now)

    class Meta:
        db_table = 'subscription'

    def __str__(self):
        return self.user.username


class UserQuota(models.Model):
    """
    Промежуточная таблица, где храним, сколько запросов
    осталось конкретному пользователю по конкретной квоте.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    requests_left = models.PositiveIntegerField(default=5)

    class Meta:
        db_table = 'user_quota'

    def __str__(self):
        return f'{self.user.email} - Quote: {self.requests_left}'