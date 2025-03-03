from django.db import models
from django.db import models
import uuid

class EmployeeType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employeetypemaster'

class Designation(models.Model):
    name = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'designationmaster'

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'departmentmaster'


class Userauth(models.Model):
    user_id = models.CharField(max_length=13)
    username = models.CharField(unique=True,max_length=20)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'user_authenthication'
class IssueTypeMaster(models.Model):
    issue_type = models.CharField(max_length=30, null=False, blank=False, unique=True)  # issue_type cannot be null

    def __str__(self):
        return self.issue_type

    class Meta:
        db_table = 'issue_type_master'  # Set the table name explicitly


class Instructor(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('employed', 'Employed'),
        ('unemployed', 'Unemployed'),
        ('government', 'Government Worker'),
    ]
    
    BUSINESS_TYPE_CHOICES = [
        ('service', 'Service'),
        ('manufacturing', 'Manufacturing'),
    ]

    # Personal Information
    name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    current_status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    pan_number = models.CharField(max_length=10, unique=True)
    aadhar_number = models.CharField(max_length=12, unique=True)
    epf_number = models.CharField(max_length=22, blank=True, null=True)

    # Social Media Links
    facebook_profile = models.CharField(max_length=200, blank=True, null=True)
    twitter_profile = models.CharField(max_length=200, blank=True, null=True)
    instagram_profile = models.CharField(max_length=200, blank=True, null=True)
    youtube_channel = models.CharField(max_length=200, blank=True, null=True)


    # About You Section
    about_you = models.TextField(blank=True, null=True)

    # Address Information
    house_no = models.CharField(max_length=100)
    area_street = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    pincode = models.CharField(max_length=6)

    # Business/Company Information
    business_name = models.CharField(max_length=100, blank=True, null=True)
    business_type = models.CharField(max_length=15, choices=BUSINESS_TYPE_CHOICES, blank=True, null=True)
    business_address = models.CharField(max_length=200, blank=True, null=True)
    product_name = models.CharField(max_length=100, blank=True, null=True)

    # Education Information
    institution_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    passed_out_year = models.IntegerField()

    # Bank Information
    bank_name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=11)
    micr_code = models.CharField(max_length=9)
    account_number = models.CharField(max_length=18)

    # Upload Section (stored as binary data)
    profile_photo = models.BinaryField(blank=True, null=True)
    resume = models.BinaryField(blank=True, null=True)
    pan_card = models.BinaryField(blank=True, null=True)
    aadhar_card = models.BinaryField(blank=True, null=True)
    bank_passbook = models.BinaryField(blank=True, null=True)

    # Additional attributes
    attribute1 = models.CharField(max_length=100, blank=True, null=True)
    attribute2 = models.CharField(max_length=100, blank=True, null=True)
    attribute3 = models.CharField(max_length=100, blank=True, null=True)
    attribute4 = models.CharField(max_length=100, blank=True, null=True)
    attribute5 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'instructorMaster'

    def __str__(self):
        return self.name
import uuid

class TeamCategory(models.Model):
    team_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name="Team ID")
    team_category = models.CharField(max_length=50, unique=True, verbose_name="Team Category")

    def __str__(self):
        return self.team_category

    class Meta:
        db_table = 'team_category'
     
    
class CostCuttingCategoryMaster(models.Model):
    categroy_name = models.CharField(max_length=50, default='General Category')  # Default category name
    category_image = models.BinaryField(blank=True, null=True)  # Optional field

    def __str__(self):
        return self.categroy_name

    class Meta:
        db_table = 'costcuttingcategorymaster'

class dailyquestion(models.Model):
    question_id = models.CharField(max_length=35,null=True,blank=True)
    question = models.CharField(max_length=250,null=True,blank=True)
    sample_input = models.CharField(max_length=250,null=True,blank=True)
    sample_output = models.CharField(max_length=250,null=True,blank=True)
    actual_output = models.CharField(max_length=250,null=True,blank=True)
    posted_on = models.CharField(max_length=35,null=True,blank=True)
    def __str__(self):
        return self.question_id
    class Meta:
        db_table = 'Daily_challenge_questions'

class dailyquestionanswer(models.Model):
    question_gid = models.CharField(max_length=35,null=True,blank=True)
    user_id = models.CharField(max_length=35,null=True,blank=True)
    submitted_on = models.DateTimeField(auto_created=True)
    token = models.CharField(max_length=35,null=True,blank=True)

    def __str__(self):
        return self.question_gid
    class Meta:
        db_table = 'Daily_challenge_answers_submitted'

class weeklyquestion(models.Model):
    question_id = models.CharField(max_length=35,null=True,blank=True)
    question = models.CharField(max_length=250,null=True,blank=True)
    sample_input = models.CharField(max_length=250,null=True,blank=True)
    sample_output = models.CharField(max_length=250,null=True,blank=True)
    actual_output = models.CharField(max_length=250,null=True,blank=True)
    posted_on = models.CharField(max_length=35,null=True,blank=True)
    def __str__(self):
        return self.question_id
    class Meta:
        db_table = 'weekly_challenge_questions'

class weeklyquestionanswer(models.Model):
    question_gid = models.CharField(max_length=35,null=True,blank=True)
    user_id = models.CharField(max_length=35,null=True,blank=True)
    submitted_on = models.DateTimeField(auto_created=True)
    token = models.CharField(max_length=35,null=True,blank=True)

    def __str__(self):
        return self.question_gid
    class Meta:
        db_table = 'weekly_challenge_answers_submitted'

class commonquestion(models.Model):
    question_id = models.CharField(max_length=35,null=True,blank=True)
    question = models.CharField(max_length=250,null=True,blank=True)
    sample_input = models.CharField(max_length=250,null=True,blank=True)
    sample_output = models.CharField(max_length=250,null=True,blank=True)
    actual_output = models.CharField(max_length=250,null=True,blank=True)
    posted_on = models.CharField(max_length=35,null=True,blank=True)
    def __str__(self):
        return self.question_id
    class Meta:
        db_table = 'common_challenge_questions'

class commonquestionanswer(models.Model):
    question_gid = models.CharField(max_length=35,null=True,blank=True)
    user_id = models.CharField(max_length=35,null=True,blank=True)
    submitted_on = models.DateTimeField(auto_created=True)
    token = models.CharField(max_length=35,null=True,blank=True)

    def __str__(self):
        return self.question_gid
    class Meta:
        db_table = 'common_challenge_answers_submitted'



class bannerupload(models.Model):
    banner1 = models.BinaryField( null=True, blank=True)
    banner2= models.BinaryField( null=True, blank=True)
    banner3 = models.BinaryField( null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'internbanner'
        
    def __str__(self):
        return f"Banner {self.id} - {self.uploaded_at}"

class collegeRegistartion(models.Model):
    user_id=models.CharField(max_length=30,null=True,blank=True)
    Name = models.CharField(max_length=50)
    
    contact_email = models.CharField(max_length=50)
    contact_phonenumber = models.CharField(max_length=15)
    College_name = models.CharField(max_length=50)
    
    Address_line_1 = models.CharField(max_length=30)
    Area = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=6)
    status = models.CharField(max_length=300,null=True,blank=True)
    ep1 = models.CharField(max_length=300,null=True,blank=True)
    ep2 = models.CharField(max_length=300,null=True,blank=True)
    ep3 = models.CharField(max_length=300,null=True,blank=True)
    ep4 = models.CharField(max_length=300,null=True,blank=True)
    ep5 = models.CharField(max_length=300,null=True,blank=True)
    
    

    def str(self):
        return self.Name

    class Meta:
        db_table = 'College_Registartion'  # Specify custom table name here


from django.db import models

class Employee(models.Model):
    employee_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    father_husband_name = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=10, choices=[('single', 'Single'), ('married', 'Married')])
    department = models.CharField(max_length=50, choices=[('hr', 'HR'), ('it', 'IT'), ('finance', 'Finance'), ('admin', 'Admin')])
    designation = models.CharField(max_length=50, choices=[('manager', 'Manager'), ('executive', 'Executive'), ('analyst', 'Analyst'), ('assistant', 'Assistant')])
    employee_type = models.CharField(max_length=20, choices=[('permanent', 'Permanent'), ('contract', 'Contract'), ('intern', 'Intern')])
    aadhar_number = models.CharField(max_length=12, unique=True)
    pan_number = models.CharField(max_length=10, unique=True)
    uan_number = models.CharField(max_length=15, blank=True, null=True)
    contact_number = models.CharField(max_length=10)
    alternate_contact_number = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(unique=True)
    education_qualification = models.CharField(max_length=100)
    work_experience = models.CharField(max_length=100)
    date_of_join = models.DateField()
    upload_photo = models.ImageField(upload_to='employee_photos/')
    house_no = models.CharField(max_length=100)
    area_street = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    pincode = models.CharField(max_length=6)
    bank_name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=11)
    micr_code = models.CharField(max_length=9)
    account_number = models.CharField(max_length=18)

    def __str__(self):
        return self.employee_name

    class Meta:
        db_table = 'employees'
