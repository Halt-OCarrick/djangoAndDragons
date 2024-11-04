from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Creature, Character, Campaign, Event, Encounter
from .serializers import (CreatureSerializer, CharacterSerializer, CampaignSerializer,
                          EventSerializer, EncounterSerializer)


@api_view(['GET'])
def get_creatures(request):
    creatures = Creature.objects.all()
    serializer = CreatureSerializer(creatures, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_creature(request):
    serializer = CreatureSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_put_del_creature(request, pk):
    try:
        creature = Creature.objects.get(pk=pk)
    except Creature.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CreatureSerializer(creature)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CreatureSerializer(creature, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        creature.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_characters(request):
    characters = Character.objects.all()
    serializer = CharacterSerializer(characters, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_character(request):
    serializer = CharacterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_put_del_character(request, pk):
    try:
        character = Character.objects.get(pk=pk)
    except Character.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CharacterSerializer(character)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CharacterSerializer(character, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_campaigns(request):
    campaigns = Campaign.objects.all()
    serializer = CampaignSerializer(campaigns, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_campaign(request):
    serializer = CampaignSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_put_del_campaign(request, pk):
    try:
        campaign = Character.objects.get(pk=pk)
    except Campaign.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CampaignSerializer(campaign)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CampaignSerializer(campaign, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        campaign.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_encounters(request):
    encounters = Encounter.objects.all()
    serializer = EncounterSerializer(encounters, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_encounter(request):
    serializer = EncounterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_put_del_encounter(request, pk):
    try:
        encounter = Encounter.objects.get(pk=pk)
    except Encounter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EncounterSerializer(encounter)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EncounterSerializer(encounter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        encounter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_event(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_put_del_event(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventSerializer(event)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
