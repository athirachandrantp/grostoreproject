from django.contrib import admin

# Register your models here.
from adminapp.models import products_upload, admin_registration
admin.site.register(products_upload)
admin.site.register(admin_registration)
