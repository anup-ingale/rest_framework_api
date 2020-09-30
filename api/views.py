from  django.http import  HttpResponse
from  api.models import Member, Period
from .serializers import  PeriodSerializer , ItemSerializer
from rest_framework.decorators import api_view
from django.core import  serializers

# def data(request):
#     users = Member.objects.all()
#     activityperiod = Period.objects.all()
#     MemberSerialize = [ItemSerializer('json',users,many=True)]
#     PeriodSerialize = [PeriodSerializer('json',activityperiod,many=True)]
#     list_final = MemberSerialize + PeriodSerialize
#     return HttpResponse(list_final,content_type="text/json-comment-filtered")

def data(request):
    users = Member.objects.all()
    activityperiod = Period.objects.all()
    users_list = serializers.serialize('json',users)
    activityperiod_list = serializers.serialize('json',activityperiod)
    list_final = [users_list,activityperiod_list]
    return HttpResponse(list_final,content_type="text/json-comment-filtered")
