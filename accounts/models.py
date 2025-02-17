from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(
        _('email address'),
        unique=True,
        blank=True,
    )
    email_verified = models.BooleanField(
        _('email verified'),
        default=False,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def has_quota(self) -> bool:
        """
        Проверка квоты для пользователя:
        - Если у пользователя есть активная подписка => True
        - Иначе проверяем, осталось ли у него хотя бы 1 доступное обращение
        """
        from subscription.models import Subscription, UserQuota

        # Есть ли у пользователя подписка
        if Subscription.objects.filter(user=self).exists():
            return True

        # Если подписки нет, смотрим на запись в UserQuota
        user_quota = UserQuota.objects.filter(user=self).first()
        if user_quota and user_quota.requests_left > 0:
            return True

        return False

    def use_quota(self) -> None:
        """
        Снимает одну квоту (1 запрос), если пользователь не имеет подписки.
        У пользователя с подпиской запросы неограниченны, следовательно не вычитаем.
        """
        from subscription.models import Subscription, UserQuota

        # Если есть подписка - ничего не делаем
        if Subscription.objects.filter(user=self).exists():
            return

        # Если подписки нет, уменьшаем счетчик в UserQuota
        user_quota = UserQuota.objects.filter(user=self).first()
        if user_quota and user_quota.requests_left > 0:
            user_quota.requests_left -= 1
            user_quota.save()