from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('Coordinator', 'Coordinator'),
        ('Principle', 'Principle'),

    )
    email = models.EmailField(null=True, blank=True, unique=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, unique=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default='student')
    otp = models.CharField(max_length=6, null=True, blank=True)
    interests = models.ManyToManyField("InterestModel")
    is_profile_completed = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class InterestModel(models.Model):
    interest = models.CharField(max_length=100)

    def __str__(self):
        return self.interest
    
class StudentProfile(models.Model):
    DEPARTMENT_CHOICES = (
        ('it', 'Information Technology'),
        ('cs', 'Computer Science'),
        ('entc', 'Electronics and Telecommunication'),
        ('mech', 'Mechanical'),
        ('biotech', 'Biotechnology'),
        ('electrical', 'Electrical'),
        ('civil', 'Civil'),
    )
    YEAR_CHOICES = (
        ('fe', 'FE'),
        ('se', 'SE'),
        ('te', 'TE'),
        ('be', 'BE'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    prn_no = models.CharField(max_length=200, null=True, blank=True)
    prn_no = models.CharField(max_length=200, null=True, blank=True)
    prn_no = models.CharField(max_length=200, null=True, blank=True)
    prn_no = models.CharField(max_length=200, null=True, blank=True)
    prn_no = models.CharField(max_length=200, null=True, blank=True)
    prn_no = models.CharField(max_length=200, null=True, blank=True)
