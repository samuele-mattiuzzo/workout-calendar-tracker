from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.template import loader
from django.utils import timezone
from tracker.models import Session

CONTEXT = {
    "TITLE": "Workout calendar tracker",
    "DESCRIPTION": "A very simple workout tracker, calendar-style",
    "KEYWORDS": "fitness, workout, weightlifting, tracker, stats, list"
}

def _get_week_by_day(dt):
    start = dt - timezone.timedelta(days=dt.weekday())
    end = start + timezone.timedelta(days=6)
    return (start, end)

def _get_week(week_day=None):
    week_day = week_day if week_day is not None else timezone.now()
    start, end = _get_week_by_day(week_day)
    return (start, end)


def index(request):
    template = loader.get_template('frontend/index.html')
    ctx = CONTEXT.copy()

    start, end = _get_week(request.GET.get('week_day', None))
    next_week_day = previous_week_day = None
    objects = Session.objects.filter(
        date__gte=start, date__lte=end
    )

    ctx.update({
        'message': None,
        'objects': objects,
        'next_week_day': next_week_day,
        'previous_week_day': previous_week_day,
        'can_edit': request.user.is_authenticated
    })
    return HttpResponse(template.render(ctx, request))



def add_session(request):
    return redirect('frontend:index')

def delete_session(request):
    return redirect('frontend:index')

def update_session(request):
    return redirect('frontend:index')

