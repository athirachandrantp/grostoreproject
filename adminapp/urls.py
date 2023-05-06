from django.urls import path
from . import views
app_name = 'adminapp'

urlpatterns=[
    path('home/',views.adminhome,name="adminhome_html"),
    path('productupload/',views.product_uploads,name="adminproductupload_html"),
    path('productview/',views.showproduct,name="productview_html"),
    path('delete/<int:productid>',views.deleteproducts,name="deleteproduct"),
    path('update/<int:productid>',views.updateproducts,name="updateproduct"),
    path('adminaccount/',views.account,name="adminaccount_html"),
    path('adminregistration/',views.admin_register,name="adminregistration_html"),
    path('adminlogin/',views.admin_login,name="adminlogin_html"),
    path('admindetails/',views.showadmin,name="admindetails_html"),
    path('deleteth/<int:adminid>',views.deleteadmin,name="delete_admin"),
    path('adminlogout/',views.admin_logout,name="adminlogout"),
    path('adminprofile/',views.admin_profile,name="adminprofile_html")


    

]