from django import forms
from django.forms import HiddenInput
from . models import Event, EventAttendance

class EventForm(forms.ModelForm):
    # This adds helper text under the input
    event_date = forms.DateField(help_text="Please enter in YYYY-MM-DD format")

    def __init__(self,*args,**kwargs):
        super(EventForm,self).__init__(*args,**kwargs)
        # these three add placeholder-"example" inside the input
        self.fields['event_date'].widget.attrs['placeholder'] = 'e.g 2021-11-28'
        self.fields['event_time'].widget.attrs['placeholder'] = 'e.g 13:00'
        self.fields['event_location'].widget.attrs['placeholder'] = 'e.g 5054 NY-23, Oneonta, NY 13820'
        # this hides this input, we will set it equal to the user in the backend
        self.fields['event_creator'].widget = HiddenInput()

    class Meta:
        model = Event
        fields = ('title','description','event_date','event_time','event_location','event_creator')

class EventAttendanceForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(EventAttendanceForm,self).__init__(*args,**kwargs)
        self.fields['event'].widget = HiddenInput()
        self.fields['user'].widget = HiddenInput()

    class Meta:
        model = EventAttendance
        fields = ('event','user')
