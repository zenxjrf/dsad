from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from .serializers import *
from .models import *

class SuvAPI(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    def get(self,request):
        suv = Suv.objects.all()
        serializer = SuvSerializer(suv,many=True)
        return Response(serializer.data)
    def post(self,request):
        water = request.data
        serializer = SuvSerializer(data=water)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"added"})
        return Response(serializer.data)

class SuvGet(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    def put(self,request,pk):
        water = Suv.objects.get(id=pk)
        serializer = SuvSerializer(water,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"updated"})
        return Response(serializer.data)
    def delete(self,request,pk):
        water = Suv.objects.get(id=pk)
        water.delete()
        return Response({"message":"deleted"})

class MijozAPI(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    def get(self,request):
        mijoz = Mijoz.objects.all()
        serializer = MijozSerializers(mijoz,many=True)
        return Response(serializer.data)
    def post(self,request):
        mijoz = request.data
        serializer = MijozSerializers(data=mijoz)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"added"})
        return Response(serializer.data)

class MijozGet(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    def put(self,request,pk):
        mijoz = Mijoz.objects.get(id=pk)
        serializer = MijozSerializer(mijoz,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"updated"})
        return Response(serializer.data)
    def delete(self,request,pk):
        mijoz = Mijoz.objects.get(id=pk)
        mijoz.delete()
        return Response({"message":"deleted"})


class BuyurtmaAPI(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    def get(self,request):
        buyurtma = Buyurtma.objects.all()
        serializer = BuyurtmaSerializer(buyurtma,many=True)
        return Response(serializer.data)
    def post(self,request):
        buyurtma = request.data
        serializer = BuyurtmaSerializer(data=buyurtma)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"added"})
        return Response(serializer.data)


class AdminAPI(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    def get(self,request):
        admin = Admin.objects.all()
        serializer = AdminSerializer(admin,many=True)
        return Response(serializer.data)

class HaydovchiAPI(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    def get(self,request):
        haydovchi = Buyurtma.objects.all()
        serializer = HaydovchiSerializer(haydovchi,many=True)
        return Response(serializer.data)








