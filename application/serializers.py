from rest_framework import serializers
from .models import *

class IndApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndApplicationModel
        fields = '__all__'

class TeamApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamApplicationsModel
        fields = '__all__'

class TeamSeralizer(serializers.ModelSerializer):
    class Meta:
        model = TeamModel
        fields = '__all__'
