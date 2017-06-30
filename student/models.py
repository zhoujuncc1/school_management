from django.db import models
from django.forms import ModelForm, DateInput
from django.contrib.admin import widgets                                       

# Create your models here.
class Student(models.Model):
    name=models.CharField('姓名', max_length=80)
    birthday = models.DateField('生日')
    people = models.CharField('民族', max_length=80)
    school = models.CharField('学校', max_length=200)
    home_address = models.CharField('家庭地址', max_length=200)
    mother_name = models.CharField('母亲姓名', max_length=80)
    mother_work = models.CharField('母亲工作单位', max_length=200)
    father_name = models.CharField('父亲姓名', max_length=80)
    father_work = models.CharField('父亲工作单位', max_length=200)   
    start_date = models.DateField('开始日期')
    end_date = models.DateField('结束日期')
    class_name = models.CharField('班级', max_length=80)
    skill_level = models.CharField('能力水平', max_length=80)
    wechat = models.CharField('微信', max_length=80)
    qq = models.CharField('QQ', max_length=80)
    matric_date = models.DateField('入学日期')
    remarks = models.CharField('备注', max_length=300)
    def get_absolute_url(self):
        return "/student/%i/" % self.id
    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生' 

class BootstrapModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })
class StudentForm(ModelForm):

    class Meta:
        model=Student
        fields=["name","birthday","people","school","home_address","mother_name","mother_work","father_name","father_work","start_date","end_date","class_name","skill_level","wechat","qq","matric_date","remarks"]
        widgets = {
            'birthday': DateInput(attrs={'class':'datepicker'}),
            'start_date': DateInput(attrs={'class':'datepicker'}),
            'end_date': DateInput(attrs={'class':'datepicker'}),
            'matric_date': DateInput(attrs={'class':'datepicker'})
            }