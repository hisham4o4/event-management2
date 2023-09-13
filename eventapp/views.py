from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Event
from .forms import ApplicantForm


def index(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    # event is a variable
    # event contains all contets(objs) of event table
    return render(request, 'eventapp/index.html', context)


def eventdetail(request, pk):
    event_single = Event.objects.get(pk=pk)
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            applicant = form.save(commit=False)  # no need to push to DB yet
            applicant.event = event_single  # event
            applicant.save()
    form = ApplicantForm
    context = {
        'event': event_single,
        'form': form

    }
    return render(request, 'eventapp/details.html', context)
