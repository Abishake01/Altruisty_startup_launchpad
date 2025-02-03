from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Course,LectureMaterial
from Master.models import Instructor
from django.utils import timezone
import base64


def addCourseMaterial(request):
    courses = Course.objects.all()

    if request.method == 'POST':
        # Extract form data from the request    
        course_id = request.POST.get('course_id')
        lecture_name = request.POST.get('lecture_name')
        lecture_duration = request.POST.get('lecture_duration')
        intro_title = request.POST.get('intro_title')
        intro_video = request.FILES.get('intro_video')  # Handling file input for intro video
        intro_video_duration = request.POST.get('intro_video_duration')
        material_title = request.POST.get('material_title')
        material_video = request.FILES.get('material_video')  # Handling file input for material video
        video_duration = request.POST.get('video_duration')
        task = request.POST.get('task')
        reading_material_file = request.FILES.get('reading_material')  # Fetch uploaded file
        reading_material_data = None
        if reading_material_file:
            reading_material_data = reading_material_file.read()

        # Fetch the selected course object 
        course = get_object_or_404(Course,id = course_id)  # Use `id` for querying the course
        
        # Convert videos to binary if they exist
        intro_video_data = None
        if intro_video:
            intro_video_data = intro_video.read()  # Reading video into binary

        material_video_data = None
        if material_video:
            material_video_data = material_video.read()  # Reading video into binary

        # Create and save a new LectureMaterial object
        lecture_material = LectureMaterial(
            course=course,  # Passing the actual course object
            lecture_name=lecture_name,
            lecture_duration=lecture_duration,
            intro_title=intro_title,
            intro_video=intro_video_data,  # Storing the binary data
            intro_video_duration=intro_video_duration,
            material_title=material_title,
            material_video=material_video_data,  # Storing the binary data
            video_duration=video_duration,
            task=task,
            reading_material=reading_material_data,
            created_date=timezone.now(),  # Automatically set created_date to now
            # Optional attributes; if not provided, they will be None
            attribute1=None,
            attribute2=None,
            attribute3=None,
            attribute4=None,
            attribute5=None,
        )

        # Save the new lecture material record to the database
        lecture_material.save()

        # Redirect to a success page or any other page after saving
          # Replace 'success_url' with the URL you want to redirect to

    # If the request is not a POST request, just render the form
    return render(request, 'Courses/add-course-materials-form.html', {'courses': courses})

def addCourseForm(request):
    if request.method == "POST":
        try:
            instructor_id = request.POST.get('instructor')
            instructor = Instructor.objects.get(id=instructor_id)

            # Check if files were provided and read them as binary
            course_image_box = request.FILES.get('course_image_box').read() if 'course_image_box' in request.FILES else None
            course_image_list = request.FILES.get('course_image_list').read() if 'course_image_list' in request.FILES else None
            course_intro_video = request.FILES.get('course_intro_video').read() if 'course_intro_video' in request.FILES else None

            # Create and save the Course object
            course = Course(
                course_title=request.POST['course_title'],
                skill_level=request.POST['skill_level'],
                category=request.POST['category'],
                instructor=instructor,
                deadline=request.POST['deadline'],
                language=request.POST['language'],
                short_description=request.POST['short_description'],
                about_course=request.POST['about_course'],
                what_we_learn=request.POST['what_we_learn'],
                price = request.POST['price'],
                course_image_box=course_image_box,
                course_image_list=course_image_list,
                course_intro_video=course_intro_video,
                attribute1=None,
                attribute2=None,
                attribute3=None,
                attribute4=None,
                attribute5=None,
            )

            course.save()
            messages.success(request, 'Course added successfully!')
            # Adjust this to your desired redirect URL

        except Instructor.DoesNotExist:
            messages.error(request, 'Instructor not found.')
              # Redirect back to the form in case of error

    # If GET request, render the form
    instructors = Instructor.objects.all()
    return render(request, 'Courses/courseForm.html', {'instructors': instructors})


def course_list(request):
    courses = Course.objects.all()
    
    # Decode binary fields to display in templates
    for course in courses:
        if course.course_image_box:
            course.course_image_box = base64.b64encode(course.course_image_box).decode('utf-8')
        if course.course_image_list:
            course.course_image_list = base64.b64encode(course.course_image_list).decode('utf-8')
        if course.course_intro_video:
            course.course_intro_video = base64.b64encode(course.course_intro_video).decode('utf-8')

    return render(request, 'Courses/course_list.html', {'courses': courses})


def view_students(request):
    
    return render(request, 'Courses/view-students.html')

def view_startup(request):
    
    return render(request, 'Courses/view-startup.html')
