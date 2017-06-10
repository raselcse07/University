from __future__ import unicode_literals
import datetime
from django.db import models


SEMESTER=[

    ("1st Semester","1st"),
    ("2nd Semester","2nd"),
    ("3rd Semester","3rd"),
    ("4th Semester","4th"),
    ("5th Semester","5th"),
    ("6th Semester","6th"),
    ("7th Semester","7th"),
    ("8th Semester","8th"),

]

SESSION=[

	("2011-12","11-12"),
	("2012-13","12-13"),
	("2013-14","13-14"),
	("2014-15","14-15"),
]

year_dropdown = []
for y in range(2007, (datetime.datetime.now().year + 12)):
    year_dropdown.append((y, y))


class Department(models.Model):

	dept_name		=models.CharField(max_length=250,unique=True,primary_key=True)
	short_name 		=models.CharField(max_length=50,unique=True)


	class Meta:

		ordering=["dept_name"]
		verbose_name_plural="Departments"
		verbose_name="Department"


	def __str__(self):

		return self.short_name

class Batch(models.Model):

	batch_session		=models.CharField(max_length=100,choices=SESSION)
	dept_name			=models.ForeignKey(Department,on_delete=models.CASCADE)


	class Meta:

		ordering=["dept_name"]
		
	def __str__(self):

		return self.batch_session


class Students(models.Model):


	student_name	=models.CharField(max_length=250)
	reg_number		=models.CharField(max_length=50,unique=True,primary_key=True)
	fathers_name	=models.CharField(max_length=250)
	mothers_name	=models.CharField(max_length=250)
	dept_name		=models.ForeignKey(Department,on_delete=models.CASCADE)
	batch_session	=models.CharField(max_length=50,choices=SESSION)
	birthday    	=models.CharField(max_length=250,help_text="Format : DD/MM/YYYY,Example : 01/01/1960")
	semester		=models.CharField(max_length=50,choices=SEMESTER)
	dist			=models.CharField(max_length=100)
	admission_year	=models.IntegerField(("Admission Year"),choices=year_dropdown,default=datetime.datetime.now().year)


	class Meta:

		ordering=["reg_number"]
		verbose_name_plural="Students"
		verbose_name="Student"


	def __str__(self):

		return str(self.reg_number)



