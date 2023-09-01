
from django.shortcuts import render
from .models import stakan, eshik
from django.http import JsonResponse
from .serializer import stakanSerializer, eshikSerializer

# Create your views here.

def all(request):
    all=stakan.objects.all()
    result=stakanSerializer(all, many=True)
    # for i in x:   
    #     y.append({
    #         'name':i.name,
    #         'hajmi':i.hajmi
    #     })
    return JsonResponse(result.data, safe=False)
    


def detail(request, realid):
    some = eshik.objects.filter(id=myid)
    forgett = eshikSerializer(some, many=True)
    return JsonResponse(forgett.data, safe=False)
        
