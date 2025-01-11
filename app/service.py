from subscription.models import Subscription

from django.http.request import HttpRequest
from django.shortcuts import render

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

class MainPage:
    def __init__(self, request: HttpRequest):
        self.request = request

        self.user = request.user
        self.subscriptions = False

    def check_auth(self):
        if self.user.is_authenticated:
            return True
        else:
            return False

    def get_subscriptions(self):
        if self.check_auth():
            self.subscriptions = Subscription.objects.get(user=self.user)
            if self.subscriptions:
                start_day = self.subscriptions.start_date
                expired = datetime.now(tz=ZoneInfo('Europe/Moscow')) - timedelta(days=31)

                if start_day > expired:
                    self.subscriptions = True


    def render(self):
        auth = self.check_auth()
        if auth:
            return render(self.request, 'TestSearch.html')
        else:
            return render(self.request, 'NoAuth.html')