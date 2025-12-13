from django.db import models
from django.utils.timezone import localtime, now
import datetime


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
            return stay_time
        else:
            stay_time = leaved_at - entered_time
            return stay_time

    def format_duration(self, duration):
        seconds = duration.total_seconds()
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        need_format = f'{hours}:{minutes}'
        return need_format

    def is_visit_long(self, minutes=60):
        if self.leaved_at is None:
            return "Визит ещё не окончен."
        else:
            time_visit = self.get_duration()
            seconds = time_visit.total_seconds()
            visit_minutes = seconds // 60
            if visit_minutes < minutes:
                return False
            else:
                return True
