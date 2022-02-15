from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email','last_name','first_name','username','date_joined','last_login','is_admin','id')
    search_fields = ('last_name','email','username')
    read_only = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    list_per_page = 50
admin.site.register(Account,AccountAdmin)
