# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-08 20:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_session', models.CharField(choices=[('2011-12', '11-12'), ('2012-13', '12-13'), ('2013-14', '13-14'), ('2014-15', '14-15')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_name', models.CharField(max_length=250, primary_key=True, serialize=False, unique=True)),
                ('short_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ['dept_name'],
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('student_name', models.CharField(max_length=250)),
                ('reg_number', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('fathers_name', models.CharField(max_length=250)),
                ('mothers_name', models.CharField(max_length=250)),
                ('batch_session', models.CharField(choices=[('2011-12', '11-12'), ('2012-13', '12-13'), ('2013-14', '13-14'), ('2014-15', '14-15')], max_length=50)),
                ('birthday', models.CharField(help_text='Format : DD/MM/YYYY,Example : 01/01/1960', max_length=250)),
                ('semester', models.CharField(choices=[('1st Semester', '1st'), ('2nd Semester', '2nd'), ('3rd Semester', '3rd'), ('4th Semester', '4th'), ('5th Semester', '5th'), ('6th Semester', '6th'), ('7th Semester', '7th'), ('8th Semester', '8th')], max_length=50)),
                ('dist', models.CharField(max_length=100)),
                ('admission_year', models.IntegerField(choices=[(2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028)], default=2017, verbose_name='Admission Year')),
                ('dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UniversityInfo.Department')),
            ],
            options={
                'ordering': ['reg_number'],
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.AddField(
            model_name='batch',
            name='dept_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UniversityInfo.Department'),
        ),
    ]
