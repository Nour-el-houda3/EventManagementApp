from django.urls import path

from .views import *
urlpatterns = [
    path('event/<str:name>', index),
    path('list/' , list_event),
    path('affiche/', ListEvents.as_view(), name="Affiche"),
    path('add/', AddEvent.as_view(), name="add"),
    path('update/<int:pk>/', updateEvent.as_view(), name="update"),
    path('delete/<int:pk>/', deleteEvent.as_view(), name="delete"),
    path('detail/<int:pk>/', detailEvent.as_view(), name="detail"),

]