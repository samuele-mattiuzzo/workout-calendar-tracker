from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.template import loader
from tracker.models import Session

CONTEXT = {
    "TITLE": "Workout calendar tracker",
    "DESCRIPTION": "A very simple workout tracker, calendar-style",
    "KEYWORDS": "fitness, workout, weightlifting, tracker, stats, list"
}


def index(request):
    template = loader.get_template('frontend/base.html')
    ctx = CONTEXT.copy()
    ctx.update({
        'message': None,
        'objects': Session.objects.all(),
        'can_edit': request.user.is_authenticated
    })
    return HttpResponse(template.render(ctx, request))

def add_session(request):
    return redirect('frontend:index')

def delete_session(request):
    return redirect('frontend:index')

def update_session(request):
    return redirect('frontend:index')

