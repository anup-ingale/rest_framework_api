from django.http import HttpResponse, JsonResponse
from  api.models import Member, Period
from django.core import  serializers
import datetime
import  json

def data(request):
    member = []
    users = Member.objects.all()
    Period.objects.all()
    for rec in users:
        temp_period = []
        for r in rec.period_set.all():
            temp_period.append({'start':str(r.start),'end':str(r.end)})
        temp_mem = {'mid': rec.mid, 'real_name': rec.real_name, 'timezone':str(rec.tz),'activity_period':temp_period}
        member.append(temp_mem)
    dict = {'ok':True,'members':member}
    return HttpResponse(json.dumps(dict),content_type="text/json-comment-filtered")


