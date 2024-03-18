from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Currently just ensures that user:username checks are case-insensitive (for registration etc)
class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        username_attr = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{username_attr: username})

class User(AbstractUser):
    objects = CustomUserManager()
    email_confirmed = models.BooleanField(default=False)
    def __unicode__(self):
        return self.username
    
class Collection(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='collections')
    monster = models.ForeignKey('Monster', on_delete=models.CASCADE, related_name='collections')
    def __str__(self):
        return self.name
    
class Monster(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='monsters')
    type = models.ForeignKey('MonsterType', on_delete=models.CASCADE, related_name='monsters')
    obtained = models.DateTimeField(auto_now_add=True)
    # Add stats here at some point.... maybe
    def __str__(self):
        return self.name

class MonsterType (models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    picture = models.CharField(max_length=200, null=False, blank=False, default='../images/Monsters/Blob.svg')
    description = models.TextField(null=True, blank=True)
    # Add base stats here at some point.... maybe
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    type = models.ForeignKey('TaskType', on_delete=models.CASCADE, related_name='tasks')
    task_description = models.TextField(null=True, blank=True)
    verify_instructions = models.TextField(null=True, blank=True)
    verify_example_pic = models.TextField(null=True, blank=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='tasks')
    # reward = models.CharField(max_length=200, null=False, blank=False, default='XP')
    monster_slot1 = models.ForeignKey('MonsterType', on_delete=models.CASCADE, related_name='task_slot1', null=True, blank=True)
    monster_slot1_chance = models.IntegerField(null=True, blank=True, default=100)
    monster_slot2 = models.ForeignKey('MonsterType', on_delete=models.CASCADE, related_name='task_slot2', null=True, blank=True)
    monster_slot2_chance = models.IntegerField(null=True, blank=True, default=100)
    def __str__(self):
        return self.name
    
class TaskType(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name
    
class Location(models.Model):
    name=models.CharField(max_length=200, null=False, blank=False, unique=True)
    type = models.ForeignKey('LocationType', on_delete=models.CASCADE, related_name='locations')
    gps = models.CharField(max_length=200, null=False, blank=False, default='0,0')
    # picture = models.CharField(max_length=200, null=False, blank=False, default='../images/Locations/Default.svg')
    description = models.TextField(null=True, blank=True)
    task_slot1 = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='location_slot1', null=True, blank=True)
    task_slot2 = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='location_slot2', null=True, blank=True)
    task_slot3 = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='location_slot3', null=True, blank=True)
    def __str__(self):
        return self.name
    
class LocationType(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name
    
class TaskVerification(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='verifications')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='verifications')
    gps = models.CharField(max_length=200, null=False, blank=False, default='0,0')
    photo = models.CharField(max_length=200, null=False, blank=False, default='../images/DefaultPhoto.svg')
    date_created = models.DateTimeField(auto_now_add=True)
    date_verified = models.DateTimeField(null=True, blank=True)
    verified = models.BooleanField(default=False)
    def __str__(self):
        return self.name