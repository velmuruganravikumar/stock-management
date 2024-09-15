from django.db import models
from django.contrib.auth.models import User


class addAdmin(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)
    mobile=models.IntegerField(null=False,blank=False)
    email=models.EmailField()
    password=models.IntegerField(null=False,blank=False)
    re_Enter_Password=models.IntegerField(null=False,blank=False)
    confirm_Password=models.IntegerField(null=False,blank=False)
    address=models.CharField(max_length=50,null=False,blank=False)
    city=models.CharField(max_length=50,null=False,blank=False)
    district=models.CharField(max_length=50,null=False,blank=False)
    
class addCategories(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name

class products(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    category=models.CharField(max_length=100,default="Unknown", null=False,blank=False)
    
    def __str__(self):
        return self.name
    
class invoiceEntry(models.Model):
    supplier_name = models.CharField(max_length=255, default='Unknown Supplier')
    date=models.DateField(null=True,blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(default='example@example.com')
    invoice_number=models.IntegerField(null=False,blank=False)
    select_category=models.CharField(max_length=50,null=False,blank=False) 
    select_product=models.CharField(max_length=50,null=False,blank=False)
    qty = models.IntegerField(default=0)
    rate=models.IntegerField(null=False,blank=False)
    gst_percentage = models.DecimalField(max_digits=5, decimal_places=2, help_text="GST percentage")
    gst_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_amound = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    mrp=models.IntegerField(null=False,blank=False)
    
    
class addClient(models.Model):
    client_name=models.CharField(max_length=50,null=False,blank=False)
    shop_name=models.CharField(max_length=50,null=False,blank=False)
    mobile=models.IntegerField(null=False,blank=False)
    location=models.CharField(max_length=50,null=False,blank=False)


class clientSales(models.Model):
    client=models.CharField(max_length=50,null=False,blank=False)
    shop=models.CharField(max_length=50,null=False,blank=False)
    select_category=models.CharField(max_length=50,null=False,blank=False)
    select_product=models.CharField(max_length=50,null=False,blank=False)
    date=models.DateField(null=True,blank=True)
    mrp=models.IntegerField(default=0)
    qty=models.IntegerField(default=0)
    rate=models.IntegerField(default=0)
    total=models.IntegerField(default=0)
    
    def __str__(self):
        return self.client
    
    
class customerSales(models.Model):
    customer_name=models.CharField(max_length=100,null=False,blank=False)
    date=models.DateField(null=False,blank=False)
    mobile=models.IntegerField(null=False,blank=False)
    location=models.CharField(max_length=100,null=False,blank=False)
    select_category=models.CharField(max_length=100,null=False,blank=False)
    select_product=models.CharField(max_length=100,null=False,blank=False)
    mrp=models.IntegerField(default=0)
    qty=models.IntegerField(default=0)
    rate=models.IntegerField(default=0)
    total=models.IntegerField(default=0)
    
    def __str__(self):
      return self.customer_name
  
    