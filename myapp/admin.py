from django.contrib import admin
from .models import addCategories,products,invoiceEntry,addClient,addAdmin,clientSales,customerSales

admin.site.register(addCategories)
# admin.site.register(products)
admin.site.register(invoiceEntry)
admin.site.register(addClient)
admin.site.register(addAdmin)
admin.site.register(clientSales)
admin.site.register(customerSales)



# class adminAddAcc(admin.ModelAdmin):
#     admin_details = ['name','mobile','email','password','re_Enter_Password','confirm_Password','address','city',' district']
# admin.site.register(addAdmin,adminAddAcc)


# class add_Categories(admin.ModelAdmin):
#     categories_details = ['name']
# admin.site.register(addCategories,add_Categories)

class add_product(admin.ModelAdmin):
   product_details = ['name','category']
admin.site.register(products,add_product)

# class invoice_entry(admin.ModelAdmin):
#     invoiceEntry_details=['suplier_name','date','mobile','email','invoice_number','select_category', 'select_product','qty', 'rate', 'gst_percentage', ' gst_amount', 'total_amound','mrp', ]
# admin.site.register(invoiceEntry,invoice_entry)

# class clientadd(admin.ModelAdmin):
#     client_detailes=['client_name','shop_name','mobile','location']



# class Salesclient(admin.ModelAdmin):
#     clientSales_details=['client_name', 'date', 'mobile', 'shop_name', 'select_category', 'select_product', 'mrp', 'qty', 'rate', 'total_amound' ]
# admin.site.register(Salesclient,clientSales)
