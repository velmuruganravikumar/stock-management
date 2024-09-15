"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    
    path('',views.login_page, name="login"),
    path('logout',views.close, name='logout'),    
    path('navbar',views.navbar, name='navbar'),
    path('dashboard',views.dashboard, name='dashboard'),
    
    
    
    path('adminmng/',views.manage_Admin, name='adminmng'),
    path('addadmin/',views.add_admin, name='addadmin'),
    path('submit/',views.submit, name='submit'),
    path('update/<int:id>', views.update_view, name='update'),
    path('delete/<int:id>', views.delete_view, name='delete'),
    
    

    
    path('addcategories/',views.add_categories, name='addcategories'),
    path('managecategories/',views.manage_categories, name='managecategories'),
    path('save/',views.save, name='save'),
    path('categorie_update/<int:id>', views.update_categories, name='categorie_update'),
    path('categorie_delete/<int:id>', views.delete_categories, name='categorie_delete'),
    
    
    path('addproducts/',views.add_products, name='addproducts'),
    path('manageproducts/',views.manage_products, name='manageproducts'),
    path('submit_product/',views.add_submit, name='submit_product'),
    path('product_update/<int:id>', views.product_update, name='product_update'),
    path('product_delete/<int:id>', views.product_delete, name='product_delete'),
    
    path('manage_invoice/',views.manage_invoice, name='manage_invoice'),
    path('create_invoice/',views.create_Invoice, name='create_invoice'),
    path('search_invoice/',views.search_Invoice, name='search_invoice'),
    path('update_invoice/<int:id>',views.update_Invoice, name='update_invoice'),
    path('delete_invoice/<int:id>',views.delete_Invoice, name='delete_invoice'),
    
    
    path('add_client/',views.add_Client, name='add_client'),
    path('client_Sales/',views.client_Sales, name='client_Sales'),
    path('client_Details/',views.client_Details, name='client_Details'),
    path('update_client/<int:id>',views.update_client, name='update_client'),
    path('delete_client/<int:id>',views.delete_client, name='delete_client'),
    # path('clientsales_manage/',views.clientSales_manage, name='clientsales_manage'),
    path('clientsales_filter/',views.clientsales_filter,name="clientsales_filter"),
    
    path('customer_Sales/',views.customer_Sales, name='customer_Sales'),
    path('customermanage/',views.customer_manage, name='customermanage'),
    
    path('stock_Report/',views.stock_Report, name='stock_Report'),
    
    path('customer_bill/',views.customer_bill, name='customer_bill'),
    path('customerbillview/',views.customerbillview, name='customerbillview'),
    
    path('total_Client_Sales/',views.total_Client_Sales, name='total_Client_Sales'),
    path('total_Customer_Sales/',views.total_Customer_Sales, name='total_Customer_Sales'),
    
    
]