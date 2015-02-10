from django.contrib import admin

# Register your models here.
from  models import *
class UserAdmin(admin.ModelAdmin):
	list_display = ('username','email')
admin.site.register(Users,UserAdmin)
