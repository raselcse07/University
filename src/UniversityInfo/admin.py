from django.contrib import admin
from .models import Department,Students,Batch


class DepartmentModelAdmin(admin.ModelAdmin):

	list_display=["dept_name"]
	list_display_links=["dept_name"]
	list_filter=["dept_name"]
	search_fields=["dept_name"]


	class Meta:

		model=Department

class StudentModelAdmin(admin.ModelAdmin):

	list_display=["reg_number","student_name","dept_name","semester","batch_session"]
	list_display_links=["reg_number","student_name","dept_name","semester","batch_session"]
	list_filter=["semester","semester","dept_name","semester","batch_session"]
	search_fields=["reg_number","student_name","dept_name","semester","batch_session"]


	class Meta:

		model=Students

class BatchModelAdmin(admin.ModelAdmin):

	list_display=["batch_session","dept_name"]
	list_display_links=["batch_session","dept_name"]
	list_filter=["batch_session","dept_name"]
	search_fields=["batch_session","dept_name"]
	
	class Meta:

		model=Batch

admin.site.register(Department,DepartmentModelAdmin)
admin.site.register(Students,StudentModelAdmin)
admin.site.register(Batch,BatchModelAdmin)

