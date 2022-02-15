from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Event, EventAttendance
from . forms import EventForm, EventAttendanceForm
from datetime import date

# Create your views here.

# ============
#  All Events
# ============
@login_required(redirect_field_name='next', login_url='signin')
def all_events_view(request):
    events = Event.objects.all()

    if request.POST:
        event_form = EventForm(data=request.POST)
        if event_form.is_valid():
            event_form.save()
        return redirect('all_events')

    event_form = EventForm(initial={'event_creator': request.user})

    context = {
        'events': events,
        'event_form': event_form,
    }

    return render(request, 'events.html', context)



# ==============
#  Single Event
# ==============
@login_required(redirect_field_name='next', login_url='signin')
def single_event_view(request,id):

    event_id = Event.objects.get(id=id)
    event_attendance = EventAttendance.objects.filter(event=id)

    is_user_going = False
    for ea in event_attendance:
        if str(ea)==str(request.user):
            is_user_going = True


    if request.POST:
        event_attendance_form = EventAttendanceForm(data=request.POST)
        if event_attendance_form.is_valid():
            event_attendance_form.save()
        event_id.attendace += 1
        event_id.save()
        return redirect(request.path_info)

    event_attendance_form = EventAttendanceForm(initial={'event':id,'user': request.user})
    context = {
        'event_id': event_id,
        'event_attendance_form': event_attendance_form,
        'is_user_going': is_user_going,
    }
    return render(request, 'full_event.html', context)
