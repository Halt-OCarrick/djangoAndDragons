from rest_framework import serializers
from .models import Creature, Character, Campaign, Event, Encounter


class CreatureSerializer(serializers.ModelSerializer):
    encounter = serializers.PrimaryKeyRelatedField(read_only=True, many=True, required=False)

    def create(self, validated_data):
        try:
            encounters = self.initial_data['encounter']
            encounters_instances = [Encounter.objects.get(pk=encounter['id']) for encounter in encounters]
            creature = Creature.objects.create(**validated_data)
            creature.encounter.set(encounters_instances)
            return creature
        except KeyError:
            return validated_data

    class Meta:
        model = Creature
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    campaign = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    def create(self, validated_data):
        campaigns = self.initial_data['campaign']
        campaigns_instances = [Campaign.objects.get(pk=campaign['id']) for campaign in campaigns]
        character = Character.objects.create(**validated_data)
        character.campaign.set(campaigns_instances)
        return character

    class Meta:
        model = Character
        fields = '__all__'


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    encounter = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    def create(self, validated_data):
        encounters = self.initial_data['encounter']
        encounters_instances = [Encounter.objects.get(pk=encounter['id']) for encounter in encounters]
        event = Event.objects.create(**validated_data)
        event.encounter.set(encounters_instances)
        return event

    class Meta:
        model = Event
        fields = '__all__'


class EncounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encounter
        fields = '__all__'
