from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from django.utils.timezone import localtime, now


def storage_information_view(request):
    non_closed_visits = []
    not_leaved_visiters = Visit.objects.filter(leaved_at__isnull=True)

    for visit in not_leaved_visiters:

        visit_content = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': visit.format_duration(visit.get_duration()),
        }

        non_closed_visits.append(visit_content)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
