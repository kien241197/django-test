from django.contrib import admin
from . import models

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
 	list_display = ("name", "email", "phone", "joined_at", "company")
class CompanyAdmin(admin.ModelAdmin):
 	list_display = ("name", "address", "created_at",)
admin.site.register(models.Member, MemberAdmin)
admin.site.register(models.Company, CompanyAdmin)
