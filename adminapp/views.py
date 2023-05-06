from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def adminhome(request):
    if 'adminid' in request.session:
        admin_id = request.session['adminid']
        return render(request,"adminhome.html")
    else:
        return render(request,"adminlogin.html")

def product_uploads(request):
    message =""
    # if 'adminid' in request.session:
    #     admin_id = request.session['adminid']
    #     return render(request,"adminproductupload.html")
    # else:
    #     return render(request,"adminlogin.html")
    if request.method == "POST":
        title = request.POST['u_title']
        category = request.POST['u_category']
        quantity = request.POST['u_quantity']
        price = request.POST['u_price']
        description = request.POST['u_description']
        uploadimage = request.FILES['u_pic']
        customerdetails = products_upload(product_title = title, product_category=category, product_quantity=quantity,product_price=price, product_description=description, product_image=uploadimage)
        customerdetails.save()
        message = 'product uploaded'
    return render(request,"adminproductupload.html",{'res':message})

def showproduct(request):
    if 'adminid' in request.session:
        admin_id = request.session['adminid']
        # return render(request,"adminproductview.html")
        productdetails = products_upload.objects.all()
        return render(request,"adminproductview.html",{'products':productdetails})
    else:
        return render(request,"adminlogin.html")

   
def deleteproducts(request,productid):
    products_upload.objects.get(id=productid).delete()
    return redirect('adminapp:productview_html')

def updateproducts(request,productid):
    if request.method == "POST":
        number = request.POST['u_number']
        title = request.POST['u_title']
        category = request.POST['u_category']
        description = request.POST['u_description']
        uploadimage = request.FILES['u_pic']
        products_upload.objects.filter(id=productid).update(product_number = number, product_title = title, product_category=category, product_description=description, product_image=uploadimage)
        return redirect('adminapp:productview_html')
    update_product = products_upload.objects.get(id=productid)
    return render(request,"updateproducts.html",{'products':update_product})

def account(request):
    if 'adminid' in request.session:
        admin_id = request.session['adminid']
        return render(request,"adminaccount.html")
    else:
        return render(request,"adminlogin.html")

def admin_register(request):
    msg=""
    if request.method == "POST":
        name = request.POST['ad_name']
        address = request.POST['ad_address']
        number = request.POST['ad_number']
        username = request.POST['ad_username']
        password = request.POST['ad_password']
        confirmpassword = request.POST['ad_confirmpassword']
        adminregistration = admin_registration(adminname=name,adminaddress=address,admincontact=number,adminusername=username,adminpassword=password,adminconfirmpassword=password)
        adminregistration.save()
        msg = 'data inserted successfully'

    return render(request,"adminregistration.html",{'ad_reg':msg})

def admin_login(request):
    if request.method == "POST":
        username = request.POST['ad_username']
        password = request.POST['ad_password']
        try:
            user = admin_registration.objects.get(adminusername=username ,adminpassword=password)
            request.session['adminid']=user.id
            return redirect('adminapp:adminhome_html')

        except admin_registration.DoesNotExist:
            return render(request,"adminlogin.html",{'failed':'loginfailed'})
    return render(request,"adminlogin.html")



def admin_logout(request):
    del request.session['adminid']
    return redirect('adminapp:adminlogin_html')

def showadmin(request):
    admindetailss = admin_registration.objects.all()
    return render(request,"admindetails.html",{'admindt':admindetailss})

def deleteadmin(request,adminid):
    admin_registration.objects.get(id=adminid).delete()
    return redirect('adminapp:admindetails_html')

def admin_profile(request):
    return render(request,"adminprofile.html")













