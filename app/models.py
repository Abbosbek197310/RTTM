from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Adti(models.Model):
    nomi=models.CharField(max_length=200 )
    yili=models.CharField(max_length=100)
    malumot=models.TextField()
    rasm=models.ImageField(upload_to='media/')
    fayl=models.FileField()
    publish = models.DateTimeField(auto_now_add=True)
    uplish = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nomi

class Rttm_malumot(models.Model):
    malumot=models.TextField()
    rasim=models.ImageField(upload_to='media/')
    def __str__(self):
        return self.malumot

class Prorektor(models.Model):
    lavozim_nomi  = models.CharField(max_length=100)
    ism=models.CharField(max_length=100)
    malumot=models.TextField()
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    rasim=models.ImageField(upload_to='media/')
     
    def __str__(self):
        return self.ism
    

class ATM_raxbar(models.Model):
    lavozim_nomi  = models.CharField(max_length=100)
    ism=models.CharField(max_length=100)
    malumot=models.TextField()
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    rasim=models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.ism  
    



class Xodimlari(models.Model):
    ism1=models.CharField(max_length=100)
    lavozimi=models.CharField(max_length=100)
    text=models.TextField()
    phone=models.CharField(max_length=50)
    rasim=models.ImageField(upload_to='media/')

    def __str__(self):
        return self.ism1
    

   

class Servis(models.Model):
    nomi=models.CharField(max_length=100)
    malumot=models.TextField()
    
    def __str__(self):
        return self.nomi
    
class Foto(models.Model):
    bino=models.CharField(max_length=50)
    xona=models.CharField(max_length=50)
    rasim=models.ImageField(upload_to='media/')

    def __str__(self):
        return self.bino  

class Kompyuter(models.Model):
    nomi=models.CharField(max_length=100)
    soni=models.IntegerField()
    def __str__(self):
        return self.nomi
    
    

     
   
    


    

    

    
    


    