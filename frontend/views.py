import pdb

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


def _get_month(month, year):
    start = timezone.datetime(year, month, 1)
    if month == 12:
        end = timezone.datetime(year, month, 31)
    else:
        end = timezone.datetime(year, month + 1, 1) + timezone.timedelta(days=-1)
    return (start, end)

def _get_week(week_day):
    start, end = _get_week_by_day(week_day)
    return (start, end)

def _get_week_by_day(dt):
    start = dt - timezone.timedelta(days=dt.weekday())
    end = start + timezone.timedelta(days=6)
    return (start, end)

def _get_previous_week_start(dt):
    previous_week_date = dt - timezone.timedelta(days=7)
    return _get_week(previous_week_date)[0]

def _get_next_week_start(dt):
    next_week_date = dt + timezone.timedelta(days=7)
    return _get_week(next_week_date)[0]

def _date_to_str_format(dt):
    return dt.strftime("%d-%m-%Y")

def index(request):
    template = loader.get_template('frontend/index.html')
    ctx = CONTEXT.copy()

    week_day = request.GET.get('week_day', None)
    link_current_week = False if week_day is None else True
    week_day = timezone.now() if week_day is None else timezone.datetime.strptime(week_day, "%d-%m-%Y").date()
    
    start, end = _get_week(week_day)

    ctx.update({
        'message': None,
        'can_edit': request.user.is_authenticated,
        'link_current_week': link_current_week,
        'start': _date_to_str_format(start),
        'end': _date_to_str_format(end),
        'next_week_day': _date_to_str_format(_get_next_week_start(start)),
        'previous_week_day': _date_to_str_format(_get_previous_week_start(start)),
        'objects': Session.objects.filter(
            date__date__gte=start, date__date__lte=end
        ).order_by('date')
    })
    return HttpResponse(template.render(ctx, request))

def index_month(request):
    # stupid! does not account for years
    template = loader.get_template('frontend/index_month.html')
    ctx = CONTEXT.copy()

    month = request.GET.get('month', None)
    link_current_month = False if month is None else True
    month = timezone.now().month if month is None else int(month)

    year = timezone.now().year
    if month < 1:
        year = year - 1
        month = 12
    elif month > 12:
        year = year + 1
        month = 1
    
    start, end = _get_month(month, year)

    ctx.update({
        'message': None,
        'can_edit': request.user.is_authenticated,
        'link_current_month': link_current_month,
        'start': _date_to_str_format(start),
        'end': _date_to_str_format(end),
        'next_month': int(month) + 1,
        'previous_month': int(month) - 1,
        'objects': Session.objects.filter(
            date__date__gte=start, date__date__lte=end
        ).order_by('date')
    })
    return HttpResponse(template.render(ctx, request))

def add_session(request):
    return redirect('frontend:index')

def delete_session(request):
    return redirect('frontend:index')

def update_session(request):
    return redirect('frontend:index')

