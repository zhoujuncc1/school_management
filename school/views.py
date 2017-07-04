from django.shortcuts import render
from .models import School
# Create your views here.
def school_processor(request):
    school = School.objects.get(pk=1)
    if bool(school.background):
        school_background = school.background.url
    else:
        school_background = '/'
    return {'school_name': school.name, 'school_address': school.address,
            'school_background': school_background}
