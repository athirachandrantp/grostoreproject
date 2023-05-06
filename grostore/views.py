from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from adminapp.models import products_upload
# Create your views here.

def fun2(request):
    return render(request,"home.html")

def fun5(request):
    return render(request,"account.html")

def fun6(request):
    if 'userid' in request.session:
        user_id = request.session['userid']
        return render(request,"aboutus.html")
    else:
        return render(request,"home.html")

def add_cart(request):
    return render(request,"cart.html")

def fun9(request):
    if 'userid' in request.session:
        user_id = request.session['userid']
        prod = products_upload.objects.all()
        return render(request,"product.html",{'products':prod})
       
    else:
        return render(request,"home.html")

def fun10(request):
    return render(request,"productdetails.html")

def registration(request):
    usermsg =""
    if request.method == "POST":
        user_name = request.POST['u_name']
        user_address = request.POST['u_address']
        user_number = request.POST['u_number']
        user_dateofbirth = request.POST['u_dob']
        user_username = request.POST['u_username']
        user_password = request.POST['u_password']
        user_confirmpassword = request.POST['u_confirmpassword']
        userreg = users_registration(username= user_name, useraddress = user_address, usernumber = user_number, userdateofbirth = user_dateofbirth, userusername=user_username, userpassword = user_password, userconfirmpassword = user_password)
        userreg.save()
        usermsg = 'data inserted successfully'

    return render(request,"registration.html",{'user_reg':usermsg})

def login(request):
    if request.method == "POST":
        user_username = request.POST['us_username']
        user_password = request.POST['us_password']
        try:
            users = users_registration.objects.get(userusername=user_username , userpassword=user_password)
            request.session['userid'] = users.id
            return redirect('grostore:home_html')
        except users_registration.DoesNotExist:
            return render(request,"loginpage.html",{'userlogin':'loginfailed'})

    return render(request,"loginpage.html")

def logout(request):
    del request.session['userid']
    return redirect('grostore:home_html')




