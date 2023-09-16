from django.urls import path




from .views import (GetAllStakan,
 PostStakan,
 GetDetailStakan,
 PatchStakan, 
DeleteStakan,
 AllFunctionStakan, 
PostGetStakan)




from .views import (GetAllEshik, 
GetDetailEshik, 
PostEshik, 
PatchEshik, 
DeleteEshik, 
AllFunctionEshik, 
PostGetEshik)





urlpatterns=[
    path('GetAllStakan/', GetAllStakan.as_view()),


    
    path('GetDetailStakan/<int:pk>', GetDetailStakan.as_view()),
    path('PostStakan/', PostStakan.as_view() ),


    
    path('PatchStakan/<int:pk>', PatchStakan.as_view()),
    path('DeleteStakan/<int:pk>', DeleteStakan.as_view()),


    
    path('PostGetStakan/', PostGetStakan.as_view()),
    path('AllFunctionStakan/<int:pk>', AllFunctionStakan.as_view()),
    path('GetAllEshik/', GetAllEshik.as_view()),
    path('GetDetailEshik/<int:pk>', GetDetailEshik.as_view()),


    
    path('PostEshik/', PostEshik.as_view() ),
    path('PatchEshik/<int:pk>', PatchEshik.as_view()),
    path('DeleteEshik/<int:pk>', DeleteEshik.as_view()),


    
    path('PostGetEshik/', PostGetEshik.as_view()),
    path('AllFunctionEshik/<int:pk>', AllFunctionEshik.as_view())


]