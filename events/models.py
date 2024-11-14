from django.db import models
from users.models import InterestModel
from ckeditor.fields import RichTextField
# Create your models here.
class NullableCharField(models.CharField):
    def __init__(self, *args, max_length=500, **kwargs):
        kwargs.setdefault('null', True)
        kwargs.setdefault('blank', True)
        kwargs['max_length'] = max_length
        super().__init__(*args, **kwargs)

class Organizers(models.Model):
    organizer_name = NullableCharField(max_length=500)
    address = NullableCharField(max_length=300)  # You can specify a different max_length
    head_organizer = NullableCharField()  # Uses the default max_length=500
    contact_organizer = NullableCharField(max_length=100)
    rating = models.IntegerField(null=True, blank=True)
    org_insta = NullableCharField()
    org_linkedin = NullableCharField()

class EventModel(models.Model):
    SPORT_TYPE_CHOICES = (
        ('individual', 'INDIVIDUAL'),
        ('team', 'TEAM')
    )
    event_name = NullableCharField()
    event_organizer = models.ForeignKey(Organizers, on_delete=models.CASCADE, null=True, blank=True)
    event_description = RichTextField(null=True, blank=True)
    coordinator_name = NullableCharField()
    coordinator_contact = NullableCharField(max_length=10)
    address_url = models.URLField(null=True, blank=True)
    entry_fees = NullableCharField()
    last_date_register = models.DateTimeField(null=True, blank=True)
    event_date = models.DateTimeField(null=True, blank=True)
    sport = models.ForeignKey(InterestModel, on_delete=models.CASCADE, null=True, blank=True)
    event_image = models.ImageField(upload_to='events/', default='images/default.png')
    no_of_applicants = models.IntegerField(null=True, blank=True)
    sport_type = models.CharField(max_length=50, choices=SPORT_TYPE_CHOICES, default='individual')
    address = models.TextField(null=True, blank=True)
    price = RichTextField(null=True, blank=True)

    def __str__(self):
        return f"{self.event_name} - {self.event_organizer.organizer_name}"

class EventDate(models.Model):
    event = models.ForeignKey(EventModel, related_name="event_dates", on_delete=models.CASCADE)
    date = models.DateTimeField()  # Individual date for the event

    def __str__(self):
        return f"{self.event.event_name} - {self.date}"
