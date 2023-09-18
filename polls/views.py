
from django.shortcuts import render
from .models import stakan, eshik
from django.http import JsonResponse
from .serializer import stakanSerializer, eshikSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# # Create your views here.
# class getstakan(APIView):
#     def get(self, request):
#         bir = stakan.objects.all()
#         srr=stakanSerializer(bir, many=True)
#         return Response(srr.data)
class GetAllStakan(generics.ListAPIView):
    queryset=stakan.objects.all()
    serializer_class=stakanSerializer
    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user)
        return stakan.objects.all()





class GetDetailStakan(generics.RetrieveAPIView):
    queryset = stakan.objects.all()




    serializer_class=stakanSerializer

class PostStakan(generics.CreateAPIView):




    queryset=stakan.objects.all()
    serializer_class=stakanSerializer

    

class PatchStakan(generics.UpdateAPIView):
    queryset=stakan.objects.all()
    serializer_class=stakanSerializer





class DeleteStakan(generics.DestroyAPIView):
    queryset=stakan.objects.all()
    serializer_class=stakanSerializer





class PostGetStakan(generics.ListCreateAPIView):
    queryset=stakan.objects.all()
    serializer_class=stakanSerializer





class AllFunctionStakan(generics.RetrieveUpdateDestroyAPIView):
    queryset=stakan.objects.all()
    serializer_class=stakanSerializer



from rest_framework import generics


# def all(request):
#     all=stakan.objects.all()
#     result=stakanSerializer(all, many=True)
#     # for i in x:   
#     #     y.append({
#     #         'name':i.name,
#     #         'hajmi':i.hajmi
#     #     })
#     return JsonResponse(result.data, safe=False)
    


# def detail(request, realid):
#     some = eshik.objects.filter(id=myid)
#     forgett = eshikSerializer(some, many=True)
#     return JsonResponse(forgett.data, safe=False)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class GetAllEshik(generics.ListAPIView):


    queryset=eshik.objects.all()
    serializer_class=eshikSerializer
    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user)
        return eshik.objects.all()


class GetDetailEshik(generics.RetrieveAPIView):
    queryset = eshik.objects.all()


    serializer_class=eshikSerializer


class PostEshik(generics.CreateAPIView):
    queryset=eshik.objects.all()
    serializer_class=eshikSerializer



class PatchEshik(generics.UpdateAPIView):
    queryset=eshik.objects.all()
    serializer_class=eshikSerializer



class DeleteEshik(generics.DestroyAPIView):
    queryset=eshik.objects.all()
    serializer_class=eshikSerializer# class poststakan(APIView):
#     def post(self, request):
#         qalee=request.data
#         zordaa = stakanSerializer(data=qalee)
#         if zordaa.is_valid():
#             zordaa.save()
#             return Response(zordaa.data)
#         return Response(zordaa.errors)

class PostGetEshik(generics.ListCreateAPIView):

    queryset=eshik.objects.all()
    serializer_class=eshikSerializer



class AllFunctionEshik(generics.RetrieveUpdateDestroyAPIView):



    queryset=eshik.objects.all()


    serializer_class=eshikSerializer

# class poststakan(APIView):
#     def post(self, request):
#         qalee=request.data
#         zordaa = stakanSerializer(data=qalee)
#         if zordaa.is_valid():
#             zordaa.save()
#             return Response(zordaa.data)
#         return Response(zordaa.errors)
        
