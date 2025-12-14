from django.db import models
from django.utils.timezone import localtime, now
import datetime


SEC_IN_HOUR = 3600
SEC_IN_MIN = 60

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        current_time = localtime(now())
        entered_time = localtime(self.entered_at)
        leaved_at = localtime(self.leaved_at)

        if self.leaved_at is None:
            stay_time = current_time - entered_time
        else:
            stay_time = leaved_at - entered_time
        return stay_time

    def format_duration(self, duration):
        seconds = duration.total_seconds()
        hours = int(seconds // SEC_IN_HOUR)
        minutes = int((seconds % SEC_IN_HOUR) // SEC_IN_MIN)
        formatted_time = '{:02}:{:02}'.format(hours, minutes)
        return formatted_time

    def is_visit_long(self, minutes=60):
        time_visit = self.get_duration()
        seconds = time_visit.total_seconds()
        visit_minutes = seconds // SEC_IN_MIN
        if visit_minutes < minutes:
            return False
        else:
            return True
