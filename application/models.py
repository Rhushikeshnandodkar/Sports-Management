from django.db import models
from events.models import *
from users.models import *
# Create your models here.
class IndApplicationModel(models.Model):
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE, null=True, blank=True)
    profile = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=True, blank=True)
    stage = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)
    reviewed_by = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.event.event_name, self.profile.user.username

class TeamModel(models.Model):
    team_lead = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    team_name = models.CharField(max_length=300, null=True, blank=True)
    sport = models.ForeignKey(InterestModel, on_delete=models.CASCADE, null=True, blank=True)

class TeamApplicationsModel(models.Model):
    team = models.ForeignKey(TeamModel, on_delete=models.CASCADE, null=True, blank=True)
    stage = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)
    reviewed_by = models.CharField(max_length=300, null=True, blank=True)