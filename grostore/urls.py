from django.urls import path
from . import views
app_name = 'grostore'

urlpatterns=[
    path('home/',views.fun2,name="home_html"),
    path('account/',views.fun5,name="account_html"),
    path('aboutus/',views.fun6,name="aboutus_html"),
    path('cart/',views.add_cart,name="cart_html"),
    path('product/',views.fun9,name="product_html"),
    path('prdtdetails/',views.fun10,name="productdetails_html"),
    path('login/',views.login,name="loginpage_html"),
    path('registration/',views.registration,name="registration_html"),
    path('logout/',views.logout,name="userlogout")

    
]