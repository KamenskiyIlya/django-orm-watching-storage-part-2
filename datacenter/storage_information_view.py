from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from django.utils.timezone import localtime, now


def storage_information_view(request):
    non_closed_visits = []
    not_leaved_visiters = Visit.objects.filter(leaved_at__isnull=True)

    for visit in not_leaved_visiters:
        visiter_passcard = visit.passcard.owner_name
        entered_time = visit.entered_at
        stay_time = visit.get_duration()
        stay_time = visit.format_duration(stay_time)

        visit_content = {
            'who_entered': visiter_passcard,
            'entered_at': entered_time,
            'duration': stay_time,
        }

        non_closed_visits.append(visit_content)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
