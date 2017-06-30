from django.shortcuts import render
from .models import School
# Create your views here.
def schoolname_processor(request):
    school = School.objects.get(pk=1)
    return {'schoolname': school.name, 'schooladdress': school.address}