from django.contrib import admin
from .models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
 	list_display = ("name", "email", "phone", "joined_at",)
admin.site.register(Member, MemberAdmin)
