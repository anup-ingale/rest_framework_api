from django.http import HttpResponse, JsonResponse
from  api.models import Member, Period
from django.core import  serializers

def data(request):
    users = Member.objects.all()
    activityperiod = Period.objects.all()
    users_list = serializers.serialize('json',users)
    activityperiod_list = serializers.serialize('json',activityperiod)
    list_final = [users_list,activityperiod_list]
    return HttpResponse(list_final,content_type="text/json-comment-filtered")
