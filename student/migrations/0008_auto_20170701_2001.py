# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20170701_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(blank=True, default='', verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='student',
            name='class_name',
            field=models.CharField(blank=True, default='', max_length=80, verbose_name='班级'),
        ),
        migrations.AlterField(
            model_name='student',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.District', verbose_name='校区'),
        ),
        migrations.AlterField(
            model_name='student',
            name='end_date',
            field=models.DateField(blank=True, default='', verbose_name='结束日期'),
        ),
        migrations.AlterField(
            model_name='student',
            name='father_name',
            field=models.CharField(blank=True, default='', max_length=80, verbose_name='父亲姓名'),
        ),
        migrations.AlterField(
            model_name='student',
            name='father_work',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='父亲工作单位'),
        ),
        migrations.AlterField(
            model_name='student',
            name='home_address',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='家庭地址'),
        ),
        migrations.AlterField(
            model_name='student',
            name='matric_date',
            field=models.DateField(blank=True, default='', verbose_name='入学日期'),
        ),
        migrations.AlterField(
            model_name='student',
            name='mother_name',
            field=models.CharField(blank=True, default='', max_length=80, verbose_name='母亲姓名'),
        ),
        migrations.AlterField(
            model_name='student',
            name='mother_work',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='母亲工作单位'),
        ),
        migrations.AlterField(
            model_name='student',
            name='people',
            field=models.CharField(blank=True, default='', max_length=80, verbose_name='民族'),
        ),
        migrations.AlterField(
            model_name='student',
            name='qq',
            field=models.CharField(blank=True, default='', max_length=80, verbose_name='QQ'),
        ),
        migrations.AlterField(
            model_name='student',
            name='remarks',
            field=models.CharField(blank=True, default='', max_length=300, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='学校'),
        ),
        migrations.AlterField(
            model_name='student',
            name='skill_level',
            field=models.CharField(blank=True, default='', max_length=80, verbose_name='能力水平'),
        ),
        migrations.AlterField(
            model_name='student',
            name='start_date',
            field=models.DateField(blank=True, default='', verbose_name='开始日期'),
        ),
        migrations.AlterField(
            model_name='student',
            name='wechat',
            field=models.CharField(blank=True, default='', max_length=80, verbose_name='微信'),
        ),
    ]
