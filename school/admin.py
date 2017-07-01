from django.contrib import admin
from django.urls import reverse
from .models import School, District
# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
    	return False
    def has_delete_permission(self, request,obj=None):
    	return False

class DistrictAdmin(admin.ModelAdmin):
    pass

admin.site.register(School, SchoolAdmin)
admin.site.register(District, DistrictAdmin)
