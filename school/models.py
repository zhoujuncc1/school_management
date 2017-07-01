from django.db import models
from django.conf import settings
# Create your models here.
class District(models.Model):
    name = models.CharField("校区", max_length=80)
    address = models.CharField('地址', max_length=300)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '校区'
        verbose_name_plural = '校区'

class School(models.Model):
    name=models.CharField('校名', max_length=80)
    address = models.CharField('地址', max_length=300)
    background = models.ImageField('背景' ,null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '学校'
        verbose_name_plural = '学校'


