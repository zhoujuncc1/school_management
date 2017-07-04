from django.db import models
from django.forms import ModelForm, DateInput, Form
from django.contrib.admin import widgets                                       
from school.models import District
# Create your models here.
class Student(models.Model):
    district = models.ForeignKey('school.District', verbose_name='校区', null=True,blank=True)
    name=models.CharField('姓名', max_length=80)
    birthday = models.DateField('生日',blank=True, null=True, default='')
    people = models.CharField('民族', max_length=80,blank=True, default='')
    school = models.CharField('学校', max_length=200,blank=True, default='')
    home_address = models.CharField('家庭地址', max_length=200,blank=True, default='')
    mother_name = models.CharField('母亲姓名', max_length=80,blank=True, default='')
    mother_work = models.CharField('母亲工作单位', max_length=200,blank=True, default='')
    father_name = models.CharField('父亲姓名', max_length=80,blank=True, default='')
    father_work = models.CharField('父亲工作单位', max_length=200,blank=True, default='')
    start_date = models.DateField('开始日期',blank=True, null=True,default='')
    end_date = models.DateField('结束日期',blank=True, null=True, default='')
    class_name = models.CharField('班级', max_length=80,blank=True, default='')
    skill_level = models.CharField('能力水平', max_length=80,blank=True, default='')
    summer_suite = models.BooleanField('领取夏装',default=False)
    autumn_suite = models.BooleanField('领取秋装',default=False)
    shoes = models.BooleanField('领取鞋子',default=False)
    wechat = models.CharField('微信', max_length=80,blank=True, default='')
    qq = models.CharField('QQ', max_length=80,blank=True, default='')
    matric_date = models.DateField('入学日期',blank=True, null=True, default='')
    remarks = models.CharField('备注', max_length=300,blank=True, default='')
    
    def get_absolute_url(self):
        return "/student/%i/" % self.id

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生' 

class StudentForm(ModelForm):

    class Meta:
        model=Student
        fields=["district","name","birthday","people","school","home_address","mother_name","mother_work","father_name","father_work","start_date","end_date","class_name","skill_level","wechat","qq","matric_date","remarks","summer_suite","autumn_suite","shoes"]
        widgets = {
            'birthday': DateInput(attrs={'class':'datepicker'}),
            'start_date': DateInput(attrs={'class':'datepicker'}),
            'end_date': DateInput(attrs={'class':'datepicker'}),
            'matric_date': DateInput(attrs={'class':'datepicker'})
            }
