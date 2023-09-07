
from django.shortcuts import render
from .models import stakan, eshik
from django.http import JsonResponse
from .serializer import stakanSerializer, eshikSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class getstakan(APIView):
    def get(self, request):
        bir = stakan.objects.all()
        srr=stakanSerializer(bir, many=True)
        return Response(srr.data)

# def all(request):
#     all=stakan.objects.all()
#     result=stakanSerializer(all, many=True)
#     # for i in x:   
#     #     y.append({
#     #         'name':i.name,
#     #         'hajmi':i.hajmi
#     #     })
#     return JsonResponse(result.data, safe=False)
    


def detail(request, realid):
    some = eshik.objects.filter(id=myid)
    forgett = eshikSerializer(some, many=True)
    return JsonResponse(forgett.data, safe=False)

class poststakan(APIView):
    def post(self, request):
        qalee=request.data
        zordaa = stakanSerializer(data=qalee)
        if zordaa.is_valid():
            zordaa.save()
            return Response(zordaa.data)
        return Response(zordaa.errors)
        
