from django.urls import path;
from . import views;

app_name='Travello'
urlpatterns = [
    path('',views.homepage),
    path('destination/<int:id>',views.dest_details,name='details'),
    path('add',views.dest_add,name='add_destination'),
    path('api/dests/',views.get_all_destinations)
]