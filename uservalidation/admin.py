from django.contrib import admin
from .models import *
# Register your models here.


class UserAdminConfig(admin.ModelAdmin):
    list_display = ('email', "isWM", "isHNI")
    search_fields = ('email', "fistName", "lastName")


admin.site.register(NewUser, UserAdminConfig)
admin.site.register(WM)
admin.site.register(HNI)
admin.site.register(WMtoHNI)
