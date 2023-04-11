from django.contrib import admin
from getdata import models
# Register your models here.

admin.site.register(models.User_Info)
admin.site.register(models.Prohibition)
admin.site.register(models.Naver_Product)
admin.site.register(models.Sourcing)
admin.site.register(models.Sourcing_Product)
admin.site.register(models.Sourcing_Option_Category)
admin.site.register(models.Sourcing_Option_Deep_Category)
admin.site.register(models.Main_Images)
admin.site.register(models.Content_Images)
admin.site.register(models.Product)
admin.site.register(models.Problem_Product)
admin.site.register(models.Secret_Key)