from django.db import models


class AClist(models.Model):
    Image = models.ImageField()
    Info = models.CharField(max_length=90,blank=False)
    Rating = models.PositiveIntegerField(blank=True)
    Price = models.FloatField(blank=True,null=True)

class Buy(models.Model):
    Name=models.CharField(max_length=10)
    Phone=models.CharField(max_length=10)
    Address =models.CharField(max_length=99)



class Quotation(models.Model):
    CHOICES = (
        ('samsung','Samsung'),
        ('lg','LG'),
        ('lloyd','Lloyd'),
        ('hitachi','Hitachi'),
        ('voltas','Voltas'),
        ('bluestar','BlueStar'),
        ('haier','Haier'),
        ('daikin','Daikin'),
        ('carrier','Carrier'),
        ('mitstubishi','Mitsubishi'),
    )
    Brand = models.CharField(max_length=15,choices=CHOICES,default='Samsung')
    Tons =models.PositiveIntegerField(null=True,blank=True)
    Phone = models.CharField(max_length=10)
    Email= models.EmailField()
    Query= models.TextField(max_length=199,null=True,blank=True)
