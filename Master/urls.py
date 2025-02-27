from django.urls import path
from . import views


urlpatterns = [
    path('instructorMaster/',views.instructorMasterForm,name="instructorMaster"),
    path('instructorlist/',views.instructor_list,name="instructorlist"),
    path('ticket_issue_type/',views.ticketIssueType,name="ticket_issue_type"),
    path('team_category_master/',views.team_category,name="team_category_master"),
    path('costcategory/', views.costcategory, name="costcategory"),
    path('view-students/', views.view_students, name='view_students'),
    path('view-internship/', views.view_internship, name='view_internships'),
    path('view-startup/', views.view_startup, name="view-startup"),
    path('accept_intern/<str:pk>',views.accept_intern),
    path('reject_intern/<str:pk>',views.rejected_intern),
    path('uploaddq/',views.uploaddq,name="upload_dq"),
    path('uploadwq/',views.uploadwq,name="upload_wq"),
    path('uploadcq/',views.uploadcq,name="upload_cq"),
    path('form/', views.daily, name="daily"),
    path('formw/', views.weekly, name="weekly"),
    path('formc/', views.common, name="common"),
    path('view-colleges/',views.collegeList,name='view_colleges'),
    path('view-mentors/',views.mentorList,name='view_mentors'),
    path('add-department/', views.department_view, name='department_view'),
    path('delete_department/<int:department_id>/', views.delete_department, name='delete_department'),
    path('designation-master/', views.designation_view, name='designation_view'),
    path('delete-designation/<int:designation_id>/', views.delete_designation, name='delete_designation'),
    path('employee-type-master/', views.employee_type_view, name='employee_type_view'),
    path('delete-employee-type/<int:employee_type_id>/', views.delete_employee_type, name='delete_employee_type'),
    path('add-employee/',views.addEmployee,name='add-employee'),
]