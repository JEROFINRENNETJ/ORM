from django.db import models
from django.contrib import admin
class Blinkit(models.Model):
    user_name=models.CharField(max_length=10)
    mobile_no=models.IntegerField(primary_key=True)
    password=models.IntegerField()
    product_no=models.IntegerField()
    product_Name=models.CharField(max_length=10)
    expiry_date=models.DateField()
    available_quantity=models.IntegerField()

class BlinkitAdmin(admin.ModelAdmin):
    list_display=["user_name","mobile_no","password","product_no","product_Name","expiry_date","available_quantity"]


