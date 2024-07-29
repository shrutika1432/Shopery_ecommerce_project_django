from django.contrib import admin
from .models import *

class CatagoryAdmin(admin.ModelAdmin): # to return image's name , image, desc at the admin site
    list_display = ('name', 'image', 'description')

admin.site.register(Catagory,CatagoryAdmin)
admin.site.register(Product)
