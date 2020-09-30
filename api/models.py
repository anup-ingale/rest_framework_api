from django.db import models
from timezone_field import TimeZoneField
import  json

# Create your models here.
class Member(models.Model):
   mid = models.CharField(max_length=12)
   real_name = models.CharField(max_length=60)
   tz = TimeZoneField(default='America/Los_Angeles')

class Period(models.Model):
   member = models.ForeignKey(Member, on_delete=models.CASCADE)
   start = models.DateTimeField()
   end = models.DateTimeField()

   def query(self):
      return self.start and self.end