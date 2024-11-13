from django.urls import path

from .views import *


# TODO: remove this comment
urlpatterns = [
    path('creatures/', get_creatures, name='get_creatures'),
    path('creatures/create/', post_creature, name='post_creature'),
    path('creatures/<int:pk>', get_put_del_creature, name='get_put_del_creature'),
    path('characters/', get_characters, name='get_characters'),
    path('characters/create/', post_character, name='post_character'),
    path('characters/<int:pk>', get_put_del_character, name='get_put_del_character'),
    path('campaigns/', get_campaigns, name='get_campaigns'),
    path('campaigns/create/', post_campaign, name='post_campaign'),
    path('campaigns/<int:pk>', get_put_del_campaign, name='get_put_del_campaign'),
    path('encounters/', get_encounters, name='get_encounters'),
    path('encounters/create/', post_encounter, name='post_encounter'),
    path('encounters/<int:pk>', get_put_del_encounter, name='get_put_del_encounter'),
    path('events/', get_events, name='get_events'),
    path('events/create/', post_event, name='post_events'),
    path('events/<int:pk>', get_put_del_event, name='get_put_del_events'),
]