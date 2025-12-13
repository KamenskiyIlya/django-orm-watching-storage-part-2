from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = Passcard.objects.get(passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    for visit in passcard_visits:

        passcard_visit_content ={
            'entered_at': visit.entered_at,
            'duration': visit.format_duration(visit.get_duration()),
            'is_strange': visit.is_visit_long()
        }
        this_passcard_visits.append(passcard_visit_content)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
