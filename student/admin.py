from django.contrib import admin

from django.urls import reverse
from .models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    def view_on_site(self, obj):
        url = reverse('student:detail', args=(obj.pk,))
        return url
    search_fields= ['district__name',"name","birthday","people","school","home_address","mother_name","mother_work","father_name","father_work","start_date","end_date","class_name","skill_level","summer_suite","autumn_suite","shoes","wechat","qq","matric_date","remarks"]
    list_display = ['name', 'district', 'start_date', 'end_date']
admin.site.register(Student, StudentAdmin)
