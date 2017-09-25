from django.db import models

# Create your models here.

class BattleSet(models.Model):
    name = models.TextField(max_length=200, default='', null=True)
    year = models.IntegerField(null=True)
    battle_number = models.IntegerField(null=True)
    attacker_king = models.TextField(max_length=200, default='', null=True)
    defender_king = models.TextField(max_length=200, default='', null=True)
    attacker_1 = models.TextField(max_length=200, default='', null=True)
    attacker_2 = models.TextField(max_length=200, default='', null=True)
    attacker_3 = models.TextField(max_length=200, default='', null=True)
    attacker_4 = models.TextField(max_length=200, default='', null=True)
    defender_1 = models.TextField(max_length=200, default='', null=True)
    defender_2 = models.TextField(max_length=200, default='', null=True)
    defender_3 = models.TextField(max_length=200, default='', null=True)
    defender_4 = models.TextField(max_length=200, default='', null=True)
    attacker_outcome = models.TextField(max_length=20, null=True)
    battle_type = models.TextField(max_length=20, null=True)
    major_death = models.IntegerField(null=True)
    major_capture = models.IntegerField(null=True)
    attacker_size = models.IntegerField(null=True)
    defender_size = models.IntegerField(null=True)
    attacker_commander = models.TextField(max_length=200, default='', null=True)
    defender_commander = models.TextField(max_length=200, default='', null=True)
    summer = models.IntegerField(null=True)
    location = models.TextField(max_length=200, default='', null=True)
    region = models.TextField(max_length=200, default='', null=True)
    note = models.TextField(max_length=5000, default='', null=True)
