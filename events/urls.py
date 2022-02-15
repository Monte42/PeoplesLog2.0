from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.all_events_view, name='all_events'),
    path('events/<id>/', views.single_event_view),
]
