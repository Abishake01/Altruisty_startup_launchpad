from django.db import models
from Master.models import Instructor
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    course_id = models.CharField(max_length=10, unique=True, editable=False)
    course_title = models.CharField(max_length=100)
    skill_level = models.CharField(max_length=50, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    ])
    category = models.CharField(max_length=50, choices=[
        ('music', 'Music'),
        ('computer', 'Computer'),
        ('arts', 'Arts'),
        ('science', 'Science')
    ])
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    deadline = models.DateField()
    language = models.CharField(max_length=50, choices=[
        ('English', 'English'),
        ('Tamil', 'Tamil'),
        ('Telugu', 'Telugu'),
        ('Kannada', 'Kannada')
    ])
    short_description = models.TextField(max_length=300)
    about_course = models.TextField()
    what_we_learn = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # Binary fields for images and video
    course_image_box = models.BinaryField(blank=True, null=True)
    course_image_list = models.BinaryField(blank=True, null=True)
    course_intro_video = models.BinaryField(blank=True, null=True)

    attribute1 = models.CharField(max_length=100, blank=True, null=True)
    attribute2 = models.CharField(max_length=100, blank=True, null=True)
    attribute3 = models.CharField(max_length=100, blank=True, null=True)
    attribute4 = models.CharField(max_length=100, blank=True, null=True)
    attribute5 = models.CharField(max_length=100, blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.course_id:  # Generate course_id only if it's not already set
            last_course = Course.objects.all().order_by('id').last()
            if last_course:
                # Increment the last course_id
                new_id = int(last_course.course_id) + 1
                self.course_id = f"{new_id:010d}"  # Format as 10 digits, zero-padded
            else:
                # If no courses exist, start with 0000000001
                self.course_id = "0000000001"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.course_title} ({self.course_id})"

    class Meta:
        db_table = 'courses'



class LectureMaterial(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name="lecture_materials")
    lecture_name = models.CharField(max_length=100)
    lecture_duration = models.PositiveIntegerField(help_text=_("Duration in minutes"))

    intro_title = models.CharField(max_length=255)
    intro_video = models.BinaryField(blank=True, null=True)  # Storing intro videos as binary data
    intro_video_duration = models.PositiveIntegerField(help_text=_("Duration in minutes"))

    material_title = models.CharField(max_length=255)
    material_video = models.BinaryField(blank=True, null=True)  # Storing lecture videos as binary data
    video_duration = models.PositiveIntegerField(help_text=_("Duration in minutes"))

    task = models.TextField(blank=True, null=True)
    reading_material = models.BinaryField(blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)  # Automatically set on creation

    attribute1 = models.CharField(max_length=100, blank=True, null=True)
    attribute2 = models.CharField(max_length=100, blank=True, null=True)
    attribute3 = models.CharField(max_length=100, blank=True, null=True)
    attribute4 = models.CharField(max_length=100, blank=True, null=True)
    attribute5 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.lecture_name} ({self.course.course_title})"

    class Meta:
        db_table = "lecture_materials"
        

class StartupRegistartion(models.Model):
    user_id=models.CharField(max_length=30,null=True,blank=True)
    startup_Name = models.CharField(max_length=30)
    founder_Name = models.CharField(max_length=50)
    founded_date = models.CharField(max_length=20)
    contact_email = models.CharField(max_length=50)
    contact_phonenumber = models.CharField(max_length=15)
    sector = models.CharField(max_length=30)
    company_stage = models.CharField(max_length=30)
    employee_count = models.CharField(max_length=10)
    Funding_Received = models.CharField(max_length=30)
    Key_technology = models.CharField(max_length=50)
    Address_line_1 = models.CharField(max_length=30)
    Area = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=6)
    Focus_area = models.CharField(max_length=25)
    Funding_duration = models.CharField(max_length=15)
    Linkedin_link = models.CharField(max_length=100)
    Github_link = models.CharField(max_length=100)
    Pitch_deck_link = models.CharField(max_length=100)
    reason = models.CharField(max_length=300)
    status = models.CharField(max_length=300,null=True,blank=True)
    ep1 = models.CharField(max_length=300,null=True,blank=True)
    ep2 = models.CharField(max_length=300,null=True,blank=True)
    ep3 = models.CharField(max_length=300,null=True,blank=True)
    ep4 = models.CharField(max_length=300,null=True,blank=True)
    ep5 = models.CharField(max_length=300,null=True,blank=True)

    def __str__(self):
        return self.startup_Name

    class Meta:
        db_table = 'Startup_Registartion'  # Specify custom table name here

class MentorRegistartion(models.Model):
    user_id=models.CharField(max_length=30,null=True,blank=True)
    Mentor_Name = models.CharField(max_length=50)
    contact_email = models.CharField(max_length=100)
    contact_phonenumber = models.CharField(max_length=15)
    Expertise = models.CharField(max_length=30)
    Job_title = models.CharField(max_length=30)
    Company_organisation = models.CharField(max_length=50)
    Year_of_experience = models.CharField(max_length=5)
    Address_line_1 = models.CharField(max_length=30)
    Area = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=6)
    Focus_area = models.CharField(max_length=25)
    Available_days = models.CharField(max_length=15)
    Linkedin_link = models.CharField(max_length=100)
    Github_link = models.CharField(max_length=100)
    resume_link = models.CharField(max_length=100)
    Short_bio = models.CharField(max_length=300)
    status = models.CharField(max_length=300,null=True,blank=True)
    ep1 = models.CharField(max_length=300,null=True,blank=True)
    ep2 = models.CharField(max_length=300,null=True,blank=True)
    ep3 = models.CharField(max_length=300,null=True,blank=True)
    ep4 = models.CharField(max_length=300,null=True,blank=True)
    ep5 = models.CharField(max_length=300,null=True,blank=True)


    def __str__(self):
        return self.Mentor_Name

    class Meta:
        db_table = 'Mentor_Registartion'  # Specify custom table name here


class ElearningRegistartion(models.Model):
    user_id=models.CharField(max_length=30,null=True,blank=True)
    student_Name = models.CharField(max_length=50)
    age = models.CharField(max_length=20)
    student_dob = models.CharField(max_length=30)
    contact_email = models.CharField(max_length=50)
    contact_phonenumber = models.CharField(max_length=15)
    College_name_Company_name = models.CharField(max_length=50)
    Department_designation = models.CharField(max_length=30)
    Current_year = models.CharField(max_length=25,null=True,blank=True)
    Year_of_graduation = models.CharField(max_length=5,null=True,blank=True)
    student_skills = models.CharField(max_length=50)
    Address_line_1 = models.CharField(max_length=30)
    Area = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=6)
    Linkedin_link = models.CharField(max_length=100)
    Github_link = models.CharField(max_length=100)
    Resume_link = models.CharField(max_length=100)
    status = models.CharField(max_length=300,null=True,blank=True)
    ep1 = models.CharField(max_length=300,null=True,blank=True)
    ep2 = models.CharField(max_length=300,null=True,blank=True)
    ep3 = models.CharField(max_length=300,null=True,blank=True)
    ep4 = models.CharField(max_length=300,null=True,blank=True)
    ep5 = models.CharField(max_length=300,null=True,blank=True)
    
    

    def __str__(self):
        return self.student_Name

    class Meta:
        db_table = 'student_Registartion'  # Specify custom table name here



class InternRegistartion(models.Model):
    user_id=models.CharField(max_length=30,null=True,blank=True)
    student_Name = models.CharField(max_length=50)
    age = models.CharField(max_length=20)
    student_dob = models.CharField(max_length=30)
    contact_email = models.CharField(max_length=50)
    contact_phonenumber = models.CharField(max_length=15)
    College_name= models.CharField(max_length=50)
    Department= models.CharField(max_length=30)
    Current_year = models.CharField(max_length=25,null=True,blank=True)
    Year_of_graduation = models.CharField(max_length=5,null=True,blank=True)
    student_skills = models.CharField(max_length=50)
    Address_line_1 = models.CharField(max_length=30)
    Area = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=6)
    domain = models.CharField(max_length=25)
    duration = models.CharField(max_length=25)
    Linkedin_link = models.CharField(max_length=100)
    Github_link = models.CharField(max_length=100)
    Resume_link = models.CharField(max_length=100)
    reason = models.CharField(max_length=300)
    status = models.CharField(max_length=300,null=True,blank=True)
    ep1 = models.CharField(max_length=300,null=True,blank=True)
    ep2 = models.CharField(max_length=300,null=True,blank=True)
    ep3 = models.CharField(max_length=300,null=True,blank=True)
    ep4 = models.CharField(max_length=300,null=True,blank=True)
    ep5 = models.CharField(max_length=300,null=True,blank=True)
    
    

    def __str__(self):
        return self.student_Name

    class Meta:
        db_table = 'intern_Registartion'  # Specify custom table name here
