from django.db import models

# Create your models here.
class School(models.Model):
    name=models.CharField('校名', max_length=80)
    address = models.CharField('地址', max_length=300)
    class Meta:
        verbose_name = '学校'
        verbose_name_plural = '学校'


