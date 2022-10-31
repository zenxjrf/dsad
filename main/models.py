from django.contrib.auth.models import User
from django.db import models


class Suv(models.Model):
    brand = models.CharField(max_length=40)
    price = models.PositiveIntegerField()
    litr = models.CharField(max_length=15)
    batafsil = models.TextField()
    def __str__(self):
        return self.brand

class Mijoz(models.Model):
    name = models.CharField(max_length=25)
    number = models.PositiveIntegerField()
    adress = models.CharField(max_length=40)
    qarz = models.PositiveIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Admin(models.Model):
    name = models.CharField(max_length=25)
    age = models.PositiveIntegerField()
    worktime = models.CharField(max_length=10)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
class Haydovchi(models.Model):
    name = models.CharField(max_length=15)
    number = models.PositiveIntegerField()
    kiritilgan_sana = models.DateTimeField()

class Buyurtma(models.Model):
    miqdor = models.PositiveIntegerField()
    umumiy = models.PositiveIntegerField()
    suv = models.ForeignKey(Suv,on_delete=models.CASCADE)
    kiritilgan_sana = models.DateTimeField()
    mijoz = models.ForeignKey(Mijoz,on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin,on_delete=models.CASCADE)
    haydovchi = models.ForeignKey(Haydovchi,on_delete=models.CASCADE)

