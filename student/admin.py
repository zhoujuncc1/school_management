from django.contrib import admin

from django.urls import reverse
from .models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    def view_on_site(self, obj):
        url = reverse('student:detail', args=(obj.pk,))
        return url
admin.site.register(Student, StudentAdmin)
