from django.urls import path
from . import views


urlpatterns = [
    path('add-course/',views.addCourseForm,name="add-course"),
    path('course_list/',views.course_list,name="course_list"),
    path('add_course_material/',views.addCourseMaterial,name="add_course_material"),
    

]