from django.urls import path
from .import views

urlpatterns = [

    # event is a variable
    # event contains all contets(objs) of event table
    path('', views.index, name='index'),
    path('event-details/<int:pk>', views.eventdetail, name='eventdetails')
]
