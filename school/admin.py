from django.contrib import admin
from django.urls import reverse
from .models import School
# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name','address')
    def has_add_permission(self, request):
    	return False
    def has_delete_permission(self, request,obj=None):
    	return False

admin.site.register(School, SchoolAdmin)
