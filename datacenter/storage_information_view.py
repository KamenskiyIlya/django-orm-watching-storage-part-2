from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from django.utils.timezone import localtime, now


def storage_information_view(request):
    non_closed_visits = []
    not_leaved_visiters = Visit.objects.filter(leaved_at__isnull=True)

    for visit in not_leaved_visiters:
        current_time = localtime(now())
        entered_time = localtime(visit.entered_at)
        stay_time = str(current_time - entered_time).split('.', maxsplit=1)[0]
        visiter_passcard = visit.passcard.owner_name

        visit_content = {
            'who_entered': visiter_passcard,
            'entered_at': str(entered_time),
            'duration': stay_time,
        }

        non_closed_visits.append(visit_content)

    # non_closed_visits = [
    #     {
    #         'who_entered': 'Richard Shaw',
    #         'entered_at': '11-04-2018 25:34',
    #         'duration': '25:03',
    #     }
    # ]

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)

