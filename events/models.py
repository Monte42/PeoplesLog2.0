from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=150, blank=False)
    event_location = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=False)
    event_creator = models.ForeignKey('users.Account',on_delete=models.CASCADE)
    attendace = models.IntegerField(default=0)
    event_date = models.DateField(auto_now=False,auto_now_add=False,blank=False)
    event_time = models.TimeField(auto_now=False,auto_now_add=False,blank=False)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('event_date', 'title', 'create_date')
        verbose_name = 'event'
        verbose_name_plural = 'events'

    def __str__(self):
        return str(self.title)

    def is_still_active(self): # This checks to see if the Event already happened
        import datetime
        return datetime.date.today() < self.event_date # returns True or False
    is_still_active = property(is_still_active) # sets this result as model property that can be called



class EventAttendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True)
    user = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return str(self.user)
