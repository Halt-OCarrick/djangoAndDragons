from django.db import models


# Create your models here.
class Campaign(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField()

    def __str__(self):
        return f'{self.name} Campaign'


class Character(models.Model):
    name = models.CharField(max_length=25)
    level = models.IntegerField()
    init_bonus = models.IntegerField()
    armor_class = models.IntegerField()
    speed = models.CharField(max_length=100)
    passive_perception = models.IntegerField()
    is_concentrating = models.BooleanField()
    max_hit_points = models.IntegerField()
    temp_hit_points = models.IntegerField()
    current_hit_points = models.IntegerField()
    campaign = models.ManyToManyField(Campaign, blank=True, null=True)

    def __str__(self):
        return self.name


class Encounter(models.Model):
    name = models.CharField(max_length=50)
    campaign_id = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    summary = models.TextField()
    tactics = models.TextField()
    treasure = models.TextField()

    def __str__(self):
        return self.name


class Creature(models.Model):
    name = models.CharField(max_length=50)
    challenge_rating = models.CharField(max_length=5)
    init_bonus = models.IntegerField()
    encounter = models.ManyToManyField(Encounter, blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=50)
    init_count = models.IntegerField()
    notes = models.TextField()
    encounter = models.ManyToManyField(Encounter)

    def __str__(self):
        return self.name
