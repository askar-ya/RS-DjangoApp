# myproject/accounts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from .models import User
from subscription.models import UserQuota


@receiver(post_save, sender=User)
def create_user_quota(sender, instance, created, **kwargs):
    """
    При создании нового пользователя автоматически добавляем ему запись квоты.
    """
    if created:
        # Пытаемся получить или создать квоту "Free"

        # Привязываем пользователя к этой квоте через промежуточную модель
        UserQuota.objects.create(
            user=instance,
            requests_left=5  # начальное количество для бесплатного пользователя
        )
