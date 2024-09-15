from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import addAdmin,addCategories,products,invoiceEntry,addClient,clientSales,customerSales
from django.contrib.auth import authenticate,logout




def login_page(request):
  if request.method=="POST":
    username=request.POST.get('Username')
    password=request.POST.get('password"')
    logins=authenticate(request,username=username,password=password)
    if logins is not None:
       return redirect('login')
    return redirect('dashboard')
  
  return render(request,'log-in.html')

def close(request):
  logout(request)
  return redirect('login')


def navbar(request):
  return render(request,'navbar.html')

def dashboard(request):
  cat_count=len(addCategories.objects.all())
  pro_count=len(products.objects.all())
  
  today_sale=0
  current_day=datetime.now().day
  sales_day=clientSales.objects.all()
  for d in sales_day:
    if d.date.day ==  current_day:
       today_sale+=d.total
  
  sales_client=clientSales.objects.all()
  totalSales=0
  for sales in sales_client:
    totalSales+=sales.total
    
  customerday_sale=0
  sales_day=customerSales.objects.all()
  for c in sales_day:
    if c.date.day == current_day:
      customerday_sale+=c.total
      
  total_sale=0
  for sale in sales_day:
    total_sale += sale.total 
      
    
  
  return render(request,'dashboard.html',{'cat_count':cat_count,'pro_count':pro_count,'totalsales':totalSales,'todaysale':today_sale,'customerday_sale':customerday_sale,'total_sale':total_sale})
  
# admin account

def add_admin(request):
  return render(request,'adminaddac.html')

def submit(request):
  if request.method=='POST':
    name=request.POST.get('name')
    mobile=request.POST.get('mobile')
    email=request.POST.get('email')
    password=request.POST.get('password')
    re_Enter_Password=request.POST.get('re_Password')
    confirm_Password=request.POST.get('confirm_Password')
    address=request.POST.get('address')
    city=request.POST.get('city')
    district=request.POST.get('district')
    
    if name and mobile and email and password and re_Enter_Password and confirm_Password and address and city and district:
       addAdmin.objects.create(name=name,mobile=mobile, email= email,password=password,re_Enter_Password=re_Enter_Password,confirm_Password=confirm_Password,address=address,city=city,district=district)
       
  return redirect('adminmng')
  
def manage_Admin(request):
  showuser=addAdmin.objects.all()
  return render(request,'adminmngac.html',{'user':showuser})

def update_view(request,id):
  update=addAdmin.objects.get(id=id)
  if request.method=="POST":
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        password=request.POST.get('password')
        re_Enter_Password=request.POST.get('re_Password')
        confirm_Password=request.POST.get('confirm_Password')
        address=request.POST.get('address')
        city=request.POST.get('city')
        district=request.POST.get('district')
      
        update.name=name
        update.mobile=mobile
        update.email=email
        update.password=password
        update.re_Enter_Password=re_Enter_Password
        update.confirm_Password=confirm_Password
        update.address=address
        update.city=city
        update.district=district
        update.save()
        
        return redirect('adminmng')
  
  return render(request,'adminupdate.html',{'user_update':update})

def delete_view(request,id):
  admDelete=addAdmin.objects.get(id=id)
  admDelete.delete()
  return redirect('adminmng')

# categories

def add_categories(request):
  return render(request,'addcategories.html')

def save(request):
  if request.method=='POST':
    categorie_name=request.POST.get('add_categori')
    if categorie_name:
       addCategories.objects.create(name=categorie_name)
       
  return redirect('managecategories')

def manage_categories(request):
  showCategories=addCategories.objects.all()
  return render(request,'mngcategories.html',{'categories':showCategories})

def update_categories(request,id):
  update_cat=addCategories.objects.get(id=id)
  if request.method=='POST':
    categorie_name=request.POST.get('add_categori')
    
    update_cat.name=categorie_name
    update_cat.save()
    return redirect('managecategories')
  return render(request,'updatecategoris.html',{'cat_update':update_cat})

def delete_categories(request,id):
  delete_cat=addCategories.objects.get(id=id)
  delete_cat.delete()
  return redirect('managecategories')

# products

def add_products(request):
  select_category=addCategories.objects.all()
  return render(request,'addproducts.html',{'select':select_category})

def add_submit(request):
  if request.method=="POST":
    category=request.POST.get('selectcategory')
    name=request.POST.get('addproducts')
    
    
    product_obj=products()
    product_obj.category=category
    product_obj.name=name
    product_obj.save()
    
  return redirect('manageproducts')

def manage_products(request):
  showproducts=products.objects.all()
  return render(request,'mngproducts.html',{'mng_products':showproducts})


def product_update(request,id):
  pro_Up=products.objects.get(id=id)
  updateCategory=addCategories.objects.all()
  if request.method=="POST":
     category=request.POST.get('selectcategory')
     name=request.POST.get('addproducts')
    
     pro_Up.category=category
     pro_Up.name=name
     pro_Up.save()
     return redirect ('manageproducts')
     
  return render(request,'updateProduct.html',{'pro_up':pro_Up,'update_cat':updateCategory})

def product_delete(request,id):
  delete_pro=products.objects.get(id=id)
  delete_pro.delete()
  return redirect ('manageproducts')


# invoice

def create_Invoice(request):
    invoice_cat=addCategories.objects.all()
    invoice_pro=products.objects.all()
    if request.method=="POST":
       suplier_name=request.POST.get('suplier_name')
       date=request.POST.get('date')
       mobile=request.POST.get('mobile')
       email=request.POST.get('email')
       Invoice_number=request.POST.get('invoice_number')
       select_category=request.POST.get('select_category')
       select_product=request.POST.get('select_product')
       qty=request.POST.get('qty',0)
       rate=request.POST.get('rate',0)
       Gst_percentage=request.POST.get('gst')
      
       gst_amount=(float(Gst_percentage))/100*int(rate)
       total_amt=int(qty)*int(rate)+gst_amount
       mrp=request.POST.get('mrp')
       
      #  s_cat=addCategories.objects.get(id=select_category)
      #  s_pro=products.objects.get(id=select_product)
      
       invoice = invoiceEntry.objects.create(
         supplier_name=suplier_name,
         date=date,
         mobile=mobile,
         email=email,
         invoice_number=Invoice_number,
         select_category=select_category,
         select_product=select_product,
         qty=qty,
         rate=rate,
         gst_percentage=Gst_percentage,
         gst_amount=gst_amount,
         total_amound=total_amt,
         mrp=mrp,
         
      )
       invoice.save()
       return redirect('manage_invoice')
      
    return render(request,'createinvoice.html',{'selectCategory_inv':invoice_cat,'selectProduct_inv':invoice_pro,})

def manage_invoice(request): 
  manage_inv=invoiceEntry.objects.all()
  return render(request,'manageinvoice.html',{'manage_inv':manage_inv})

def search_Invoice(request):
  query = request.POST.get('invoice_number')
  results = []
  if query:
    results = invoiceEntry.objects.filter(invoice_number=query)
  return render(request,'searchinvoice.html',{'results':results,'query':query})
  
  
  
def update_Invoice(request,id):
  invoice_update=invoiceEntry.objects.get(id=id)
  update_categry=addCategories.objects.all()
  update_product=products.objects.all()
  
  if request.method=="POST":
      suplier_name=request.POST.get('suplier_name')
      date=request.POST.get('date')
      mobile=request.POST.get('mobile')
      email=request.POST.get('email')
      Invoice_number=request.POST.get('invoice_number')
      select_category_id=request.POST.get('select_category')
      select_product_id=request.POST.get('select_product')
      qty=request.POST.get('qty',0)
      rate=request.POST.get('rate',0)
      Gst_percentage=request.POST.get('gst')
      
      gst_amount=(float(Gst_percentage))/100*int(rate)
      total_amt=int(qty)*int(rate)+gst_amount
      mrp=request.POST.get('mrp')
      
      selectCategory=addCategories.objects.get(id=select_category_id)
      selectProduct=products.objects.get(id=select_product_id)
      
    
      invoice_update.supplier_name=suplier_name
      invoice_update.date=date
      invoice_update.mobile=mobile
      invoice_update.email=email
      invoice_update.invoice_number=Invoice_number
      invoice_update.select_category=selectCategory
      invoice_update.select_product=selectProduct
      invoice_update.qty=qty
      invoice_update.rate=rate
      invoice_update.gst_percentage=Gst_percentage
      invoice_update.gst_amount=gst_amount
      invoice_update.total_amound=total_amt
      invoice_update.mrp=mrp
      invoice_update.save()
      
      return redirect('manage_invoice')
         
  return render(request,'updateinvoice.html',{'upd_inv':invoice_update,'up_pro':update_product,'up_cat':update_categry})

def delete_Invoice(request,id):
  delete_inv = invoiceEntry.objects.get(id=id)
  delete_inv.delete()
  return redirect ('manage_invoice')

# addclient

def add_Client(request):
  if request.method=="POST":
    clientName=request.POST.get('clientname')
    shopname=request.POST.get('shopname')
    mobile=request.POST.get('mobile')
    location=request.POST.get('location')
    
    add_client=addClient.objects.create(
      client_name=clientName,
      shop_name=shopname,
      mobile=mobile,
      location=location,
    )
    add_client.save()
    return redirect('client_Details')
  return render(request,'addclient.html')

def client_Sales(request):
  select_client=addClient.objects.all()
  select_cat=addCategories.objects.all()
  select_pro=products.objects.all()
  
  if request.method=="POST":
    client_name=request.POST.get('clientname')
    shop_name=request.POST.get('shopname')
    selectCat=request.POST.get('select_category')
    selectPro=request.POST.get('select_product')
    date=request.POST.get('date')
    mrp=request.POST.get('mrp')
    qty=request.POST.get('qty')
    rate=request.POST.get('rate')
    total_amt=int(rate)*int(qty)
    
    # category_id=addCategories.objects.get(id=selectCat)
    
    
    sale_obj=clientSales()
    sale_obj.client=client_name
    sale_obj.shop=shop_name
    sale_obj.select_category=selectCat
    sale_obj.select_product=selectPro
    sale_obj.date=date
    sale_obj.mrp=mrp
    sale_obj.qty=qty
    sale_obj.rate=rate
    sale_obj.total=total_amt
    sale_obj.save()
    return HttpResponse('saved successfully')
  return render(request,'clientsalesentry.html',{'salcat':select_cat,'salpro':select_pro,'clientName':select_client})

# def clientSales_manage(request):
#   cls=clientSales.objects.all()
#   return render(request,'clientsalesmanage.html',{'cls':cls})

def clientsales_filter(request):
  query = request.POST.get('clientname')
  results = []
  if query:
    results = clientSales.objects.filter(client=query)
  return render(request, 'clientsalesfilter.html',{'results':results,'query':query})
  
  

def client_Details(request):
  clientDetails=addClient.objects.all()
  return render(request,'clientdetails.html',{'clientdatails':clientDetails})

def update_client(request,id):
  updateClient=addClient.objects.get(id=id)
  if request.method=="POST":
    clientName=request.POST.get('clientname')
    shopname=request.POST.get('shopname')
    mobile=request.POST.get('mobile')
    location=request.POST.get('location')
    
    updateClient.client_name=clientName
    updateClient.shop_name=shopname
    updateClient.mobile=mobile
    updateClient.location=location
    updateClient.save()
    return redirect('client_Details')
  return render(request,'updateclient.html',{"updateClient":updateClient})

def delete_client(request,id):
  deleteClient=addClient.objects.get(id=id)
  deleteClient.delete()
  return redirect('client_Details')

  

# customer details
def customer_Sales(request):
  select_cat=addCategories.objects.all()
  select_pro=products.objects.all()
  if request.method =="POST":
     customer_name=request.POST.get('customername')
     date=request.POST.get('date')
     mobile=request.POST.get('mobile')
     location=request.POST.get('location')
     select_cat=request.POST.get('select_category')
     select_pro=request.POST.get('select_product')
     mrp=request.POST.get('mrp')
     qty=request.POST.get('qty')
     rate=request.POST.get('rate')
     total_amt=int(rate)*int(qty)
     
     cat_id=addCategories.objects.get(id=select_cat)
     pro_id=products.objects.get(id=select_pro)
     
     customer_sales=customerSales()
     customer_sales.customer_name=customer_name
     customer_sales.date=date
     customer_sales.mobile=mobile
     customer_sales.location=location
     customer_sales.select_category=cat_id
     customer_sales.select_product=pro_id
     customer_sales.mrp=mrp
     customer_sales.qty=qty
     customer_sales.rate=rate
     customer_sales.total=total_amt
     customer_sales.save()
     
     return redirect('customermanage')
  return render(request,'customersales.html',{'select_cat':select_cat,'select_pro':select_pro})

def customer_manage(request):
  cus_manage=customerSales.objects.all()
  return render(request,'customermanage.html',{'cus_manage':cus_manage})

def stock_Report(request):
  sr_cat=invoiceEntry.objects.all()
  cl_sal=clientSales.objects.all()

  pro_qty = {}

  for i in sr_cat:
        product = i.select_product
        if product not in pro_qty:
            pro_qty[product] = i.qty
        else:
            pro_qty[product] += i.qty

  for j in cl_sal:
        product = j.select_product
        if product in pro_qty:
            pro_qty[product] -= j.qty
        else:
            pro_qty[product] = -j.qty

  pro_qty_list = zip(pro_qty.keys(),pro_qty.values())
  
      
  return render(request,'stockreport.html',{'pro_qty_list':pro_qty_list})






def customer_bill(request):
  if request.method=="POST":
    categories=request.POST.getlist('category')
    quantities=request.POST.getlist('qty')
    mrps=request.POST.getlist('mrp')
    rates=request.POST.getlist('rate')
    
    
    bill_data = []
    subtotal=0
    for i in range(len(categories)):
        total=int(quantities[i])*int(rates[i])
        bill_data.append({
              'category': categories[i],
              'qty': quantities[i],
              'mrp': mrps[i],
              'rate': rates[i],
              'total': total
              
            })
        subtotal += total
   
      
    return render(request,'customerbillview.html',{'bill_data':bill_data,'subtotal':subtotal})
  return render(request,'customerbill.html')







def customerbillview(request):
  return render(request,'customerbillview.html')

def total_Client_Sales(request):
  return render(request,'totalclientsales.html')

def total_Customer_Sales(request):
  return render(request,'totalcussales.html')



# def home(request):
#   msg="<h1>this is home page</h1>"
#   return HttpResponse(msg)

# def showtime(request):
#   time=datetime.datetime.now()
#   date_dict={"dt":time}
#   return render(request,"index.html",context=date_dict)

# def index(request):
#   return render(request,"index.html")










