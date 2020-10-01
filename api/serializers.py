from rest_framework import serializers
from .models import Member,Period


class PeriodSerializer(serializers.ModelSerializer):
    class Meta :
        model = Period
        fields ='__all__'

class ItemSerializer(serializers.ModelSerializer):
    activity_periods = serializers.RelatedField(source='Period',many=True,read_only=True)
    class Meta:
        model = Member
        fields = ('mid','real_name', 'tz', 'query')