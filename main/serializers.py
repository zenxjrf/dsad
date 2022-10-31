from rest_framework.exceptions import APIException

from .models import *
from rest_framework.serializers import ModelSerializer
from datetime import datetime


class SuvSerializer(ModelSerializer):
    class Meta:
        model = Suv
        fields = '__all__'

class MijozSerializer(ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'
    def validate_qarz(self,qarz):
        if qarz > 5000000:
            raise APIException("У вас большие долги")





class AdminSerializer(ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class HaydovchiSerializer(ModelSerializer):
    class Meta:
        model = Haydovchi
        fields = '__all__'

class BuyurtmaSerializer(ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'