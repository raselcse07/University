from django.shortcuts import render,get_object_or_404
from .models import Department,Students,Batch


def DepartmentList(request):


	qs=Department.objects.all()

	context={

		"qs":qs
	}

	template_name="UniversityInfo/dept_list.html"

	return render(request,template_name,context)


def DepartmentDetail(request,dept_name=None):

	qs=Department.objects.get(short_name=dept_name)

	session=Batch.objects.filter(dept_name=qs)

	template_name="UniversityInfo/dept_detail.html"
	context={

			"session":session,
			"qs":qs
			}

	return render(request,template_name,context)


def StudentList(request,dept_name=None,batch_session=None):

	qs=Department.objects.get(short_name=dept_name)
	qs2=Batch.objects.get(dept_name=qs,batch_session=batch_session)
	
	if qs and qs2:

		qs3=Students.objects.filter(dept_name=qs,batch_session=qs2)

	template_name="UniversityInfo/stu_list.html"
	context={"qs":qs,"qs2":qs2,"qs3":qs3}

	return render(request,template_name,context)

def StudentDetail(request,dept_name=None,batch_session=None,reg_number=None):
	
	qs=Department.objects.get(short_name=dept_name)
	qs2=Batch.objects.get(dept_name=qs,batch_session=batch_session)
	qs3=Students.objects.filter(dept_name=qs,batch_session=qs2,reg_number=reg_number)

	template_name="UniversityInfo/student_detail.html"
	context={"qs3":qs3}

	return render(request,template_name,context)


def About(request):

	template_name="UniversityInfo/about.html"

	return render(request,template_name,{})


def Contact(request):

	template_name="UniversityInfo/contact.html"

	return render(request,template_name,{})


