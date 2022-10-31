from main.views import *
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Suv/',SuvAPI.as_view()),
    path('Suvget/<int:pk>/',SuvGet.as_view()),
    path('Mijoz/',MijozAPI.as_view()),
    path('MijozGet/<int:pk>/',MijozGet.as_view()),
    path('Buyurtma/',BuyurtmaAPI.as_view()),
    path('Haydovchilar/',HaydovchiAPI.as_view()),
    path('Adminlar/',AdminAPI.as_view()),
    path('tokenget/',TokenObtainPairView.as_view()),
    path('tokenrefresh/',TokenRefreshView.as_view()),

]
