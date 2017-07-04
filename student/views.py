from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from django.forms.models import model_to_dict

from .models import Student, StudentForm
# Create your views here.

class DetailView(generic.DetailView):
    model = Student
    template_name = 'student/detail.html'

class RegisterView(generic.CreateView):
	form_class = StudentForm
	template_name = 'student/student_form.html'
