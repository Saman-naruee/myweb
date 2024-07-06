from django.shortcuts import render
from .models import Event
from datetime import datetime, timedelta
def upcoming_events(request):
    today = datetime.now().date()
    last_week_events = Event.objects.filter(date__range=[today - timedelta(days=7), today - timedelta(days=1)])
    future_events = Event.objects.filter(date__gte=today) # date__gte: date Greater Than (or) Equal

    # events = Event.objects.all()
    context = {
        'last_week_events' : last_week_events,
        'future_events' : future_events,
    }
    Path = 'events/upcoming_events.html'
    return render(request, Path, context)
