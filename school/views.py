from django.shortcuts import render
from .models import School
# Create your views here.
def school_processor(request):
    school = School.objects.get(pk=1)
    return {'school_name': school.name, 'school_address': school.address,
            'school_background': school.background}