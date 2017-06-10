from django.conf.urls import url
from . import views

app_name="UniversityInfo"

urlpatterns = [

    url(r'^$', views.DepartmentList,name="dept_list"),
    url(r'^about/$', views.About,name="about"),
    url(r'^contact/$', views.Contact,name="contact"),
    url(r'^department/(?P<dept_name>[\w-]+)/$', views.DepartmentDetail,name="dept_detail"),
    url(r'^department/(?P<dept_name>[\w-]+)/(?P<batch_session>[\w-]+)/$', views.StudentList,name="student_list"),
    url(r'^department/(?P<dept_name>[\w-]+)/(?P<batch_session>[\w-]+)/(?P<reg_number>[\w-]+)/$', views.StudentDetail,name="student_detail"),
]
