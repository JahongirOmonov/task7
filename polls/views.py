
from django.shortcuts import render
from .models import stakan, eshik
from django.http import JsonResponse

# Create your views here.

def all(request):
    x=stakan.objects.all()
    y =[]
    for i in x:   
        y.append({
            'name':i.name,
            'hajmi':i.hajmi
        })
    return JsonResponse(y, safe=False)
    


def detail(request, realid):
    each = eshik.objects.get(id=realid)
    data={'Nomi':each.nomi, 'Eshik bo`yi':each.boyi}
    return JsonResponse(data, safe=False)
        
