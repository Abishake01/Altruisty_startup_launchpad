from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Instructor,IssueTypeMaster,CostCuttingCategoryMaster, dailyquestion, dailyquestionanswer ,weeklyquestion , weeklyquestionanswer ,commonquestion , commonquestionanswer,bannerupload,Userauth,collegeRegistartion
from Courses.models import InternRegistartion, StartupRegistartion, ElearningRegistartion,MentorRegistartion
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
from django.core.mail import send_mail
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as crypto_padding
from cryptography.hazmat.backends import default_backend
import base64

from django.conf import settings
from .models import Designation
from .forms import DesignationForm
from .forms import EmployeeTypeForm
from .models import EmployeeType


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee
from django.views.decorators.csrf import csrf_exempt

def addEmployee(request):
    if request.method == 'POST':
        try:
            # Retrieve data from POST request
            employee_name = request.POST.get('employee_name')
            dob = request.POST.get('dob')
            gender = request.POST.get('gender')
            father_husband_name = request.POST.get('father_husband_name')
            marital_status = request.POST.get('marital_status')
            department = request.POST.get('department')
            designation = request.POST.get('designation')
            employee_type = request.POST.get('employee_type')
            aadhar_number = request.POST.get('aadhar_number')
            pan_number = request.POST.get('pan_number')
            uan_number = request.POST.get('uan_number', '')  # Optional field
            contact_number = request.POST.get('contact_number')
            alternate_contact_number = request.POST.get('alternate_contact_number', '')
            email = request.POST.get('email')
            education_qualification = request.POST.get('education_qualification')
            work_experience = request.POST.get('work_experience')
            date_of_join = request.POST.get('date_of_join')

            # Handle file upload
            upload_photo = request.FILES.get('upload_photo')

            house_no = request.POST.get('house_no')
            area_street = request.POST.get('area_street')
            city = request.POST.get('city')
            state = request.POST.get('state')
            country = request.POST.get('country')
            pincode = request.POST.get('pincode')


            # Bank Information
            bank_name = request.POST.get('bank_name')
            branch_name = request.POST.get('branch_name')
            ifsc_code = request.POST.get('ifsc_code')
            micr_code = request.POST.get('micr_code')
            account_number = request.POST.get('account_number')

            # Create an Employee object and save to the database
            employee = Employee(
                employee_name=employee_name,
                dob=dob,
                gender=gender,
                father_husband_name=father_husband_name,
                marital_status=marital_status,
                department=department,
                designation=designation,
                employee_type=employee_type,
                aadhar_number=aadhar_number,
                pan_number=pan_number,
                uan_number=uan_number,
                contact_number=contact_number,
                alternate_contact_number=alternate_contact_number,
                email=email,
                education_qualification=education_qualification,
                work_experience=work_experience,
                date_of_join=date_of_join,
                upload_photo=upload_photo,
                house_no=house_no,
                area_street=area_street,
                city=city,
                state=state,
                country=country,
                pincode=pincode,
                bank_name=bank_name,
                branch_name=branch_name,
                ifsc_code=ifsc_code,
                micr_code=micr_code,
                account_number=account_number,
            )

            employee.save()

            # Redirect or render a success page
            return redirect('add-employee')  # Replace 'success' with your success URL name

        except Exception as e:
            return HttpResponse(f"An error occurred: {e}", status=500)

    # Render the form for GET request
    return render(request, 'Master/addemployee.html',{'departments':Department.objects.all(),'designaions':Designation.objects.all(),'employee_types':EmployeeType.objects.all()})


def pad_data(data):
    """Pad data to make its length a multiple of 16 (block size for AES)."""
    padder = crypto_padding.PKCS7(128).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()
    return padded_data


from django.contrib import messages
from .models import Department
from .forms import DepartmentForm

def employee_type_view(request):
    # Handle form submission
    if request.method == 'POST':
        form = EmployeeTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee Type added successfully!")
            return redirect('employee_type_view')  # Redirect to the same page after success
    else:
        form = EmployeeTypeForm()

    # Fetch existing employee types to display in the table
    employee_types = EmployeeType.objects.all()

    return render(request, 'Master/employeetypemaster.html', {
        'form': form,
        'employee_types': employee_types,
    })

def delete_employee_type(request, employee_type_id):
    try:
        employee_type = EmployeeType.objects.get(id=employee_type_id)
        employee_type.delete()
        messages.success(request, f"Employee Type '{employee_type.name}' deleted successfully!")
    except EmployeeType.DoesNotExist:
        messages.error(request, "Employee Type not found.")
    return redirect('employee_type_view')

def designation_view(request):
    # Get all designations
    designations = Designation.objects.all()
    
    if request.method == 'POST' and 'designation_form' in request.POST:
        designation_form = DesignationForm(request.POST)
        if designation_form.is_valid():
            designation_form.save()
            messages.success(request, "Designation added successfully!")
            return redirect('designation_view')
    else:
        designation_form = DesignationForm()

    return render(request, 'Master/designationmaster.html', {
        'form': designation_form,
        'designations': designations,
    })

def delete_designation(request, designation_id):
    designation = get_object_or_404(Designation, id=designation_id)
    designation.delete()
    messages.success(request, "Designation deleted successfully!")
    return redirect('designation_view')

# View for creating and listing departments
def department_view(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Department added successfully!")
            return redirect('department_view')
        else:
            messages.error(request, "There was an error with the form submission.")
    else:
        form = DepartmentForm()

    # Fetch all departments
    departments = Department.objects.all()
    return render(request, 'Master/departmentmaster.html', {'form': form, 'departments': departments})

# View for deleting a department
def delete_department(request, department_id):
    department = Department.objects.get(id=department_id)
    if department:
        department.delete()
        messages.success(request, f"Department '{department.name}' deleted successfully!")
    else:
        messages.error(request, "Department not found.")
    
    return redirect('department_view')


def encrypt_data(data, key):
    """Encrypt the data using AES."""
    # Ensure the key is in bytes format
    if isinstance(key, str):
        key = key.encode()

    # Hash the key using SHA256
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(key)
    aes_key = digest.finalize()[:32]  # Use 32 bytes for AES-256

    # Generate a random IV
    iv = os.urandom(16)

    # Create cipher config with AES CBC mode
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Pad the data and encrypt
    padded_data = pad_data(data)
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Return the IV + encrypted data encoded in base64
    return base64.b64encode(iv + encrypted_data).decode()



import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as crypto_padding
from cryptography.hazmat.backends import default_backend

def decrypt_data(encrypted_data, key):
    """Decrypt the encrypted data using AES."""
    # Ensure the key is in bytes format
    if isinstance(key, str):
        key = key.encode()

    # Hash the key using SHA256
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(key)
    aes_key = digest.finalize()[:32]

    # Decode the base64 encoded data and ensure correct padding
    encrypted_data_bytes = base64.b64decode(encrypted_data)

    # Check if the length of the encrypted data is divisible by 4, if not, pad it
    if len(encrypted_data) % 4 != 0:
        encrypted_data += '=' * (4 - len(encrypted_data) % 4)

    # Decode the data again after padding
    encrypted_data_bytes = base64.b64decode(encrypted_data)

    # Extract the IV (first 16 bytes) and ciphertext (remaining data)
    if len(encrypted_data_bytes) < 16:
        raise ValueError("Received encrypted data is too short to contain IV and ciphertext.")

    iv = encrypted_data_bytes[:16]
    ciphertext = encrypted_data_bytes[16:]

    print(f"Extracted IV (hex): {iv.hex()} (Length: {len(iv)})")
    print(f"Ciphertext (hex): {ciphertext.hex()} (Length: {len(ciphertext)})")

    # Create cipher config with AES CBC mode
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt and unpad the data
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad the decrypted data
    unpadded_data = unpad_data(decrypted_data)

    return unpadded_data

def unpad_data(data):
    """Remove padding from data."""
    unpadder = crypto_padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(data) + unpadder.finalize()
    return unpadded_data.decode()

def ticketIssueType(request):
    issue_types = IssueTypeMaster.objects.all()

    if request.method == "POST" and "issue_type" in request.POST:
        # Retrieve and decrypt the encrypted issue_type from the form
        encrypted_issue_type = request.POST.get("issue_type")
        
        try:
            decrypted_issue_type = decrypt_data(encrypted_issue_type, settings.ENCRYPTION_KEY)
            return HttpResponse(f"Decrypted issue type: {decrypted_issue_type}")
        except Exception as e:
            return HttpResponse(f"Error decrypting data: {e}", status=400)

        if decrypted_issue_type:
            # Save the decrypted issue type into the database
            issue_type_instance = IssueTypeMaster(issue_type=decrypted_issue_type)
            issue_type_instance.save()

            return redirect('ticket_issue_type')  # Refresh the table

    if request.method == "POST" and 'delete' in request.POST:
        issue_type_id = request.POST.get('delete')
        try:
            issue_type_instance = IssueTypeMaster.objects.get(id=issue_type_id)
            issue_type_instance.delete()
        except IssueTypeMaster.DoesNotExist:
            pass

        return redirect('ticket_issue_type')  # Refresh the page after deletion

    return render(request, 'Master/issue_type.html', {
        'issue_types': issue_types,
        'encryption_key': settings.ENCRYPTION_KEY
    })


def instructorMasterForm(request):
    if request.method == 'POST':
        try:
            # Personal Information
            instructor_name = request.POST.get('instructor_name')
            dob = request.POST.get('dob')
            gender = request.POST.get('gender')
            phone_number = request.POST.get('phone_number')
            email = request.POST.get('email')
            current_status = request.POST.get('current_status')
            pan_number = request.POST.get('pan_number')
            aadhar_number = request.POST.get('aadhar_number')
            epf_number = request.POST.get('epf_number', None)  # Optional field

            # Address Information
            house_no = request.POST.get('house_no')
            area_street = request.POST.get('area_street')
            city = request.POST.get('city')
            state = request.POST.get('state')
            country = request.POST.get('country')
            pincode = request.POST.get('pincode')

            # Business or Company Information
            business_name = request.POST.get('business_name')
            business_type = request.POST.get('business_type')
            business_address = request.POST.get('business_address')
            product_name = request.POST.get('product_name')

            # Education Information
            institution_name = request.POST.get('institution_name')
            degree = request.POST.get('degree')
            percentage = request.POST.get('percentage')
            passed_out_year = request.POST.get('passed_out_year')

            # Bank Information
            bank_name = request.POST.get('bank_name')
            branch_name = request.POST.get('branch_name')
            ifsc_code = request.POST.get('ifsc_code')
            micr_code = request.POST.get('micr_code')
            account_number = request.POST.get('account_number')

            # Social Media Links
            facebook_profile = request.POST.get('facebook_profile', None)
            twitter_profile = request.POST.get('twitter_profile', None)
            instagram_profile = request.POST.get('instagram_profile', None)
            youtube_channel = request.POST.get('youtube_channel', None)

            # About You Section
            about_you = request.POST.get('about_you', None)

            # Uploads (read binary data)
            profile_photo = request.FILES['profile_photo'].read() if 'profile_photo' in request.FILES else None
            resume = request.FILES['resume'].read() if 'resume' in request.FILES else None
            pan_card = request.FILES['pan_card'].read() if 'pan_card' in request.FILES else None
            aadhar_card = request.FILES['aadhar_card'].read() if 'aadhar_card' in request.FILES else None
            bank_passbook = request.FILES['bank_passbook'].read() if 'bank_passbook' in request.FILES else None

            # Save to database
            instructor = Instructor(
                name=instructor_name,
                dob=dob,
                gender=gender,
                phone_number=phone_number,
                email=email,
                current_status=current_status,
                pan_number=pan_number,
                aadhar_number=aadhar_number,
                epf_number=epf_number,
                house_no=house_no,
                area_street=area_street,
                city=city,
                state=state,
                country=country,
                pincode=pincode,
                business_name=business_name,
                business_type=business_type,
                business_address=business_address,
                product_name=product_name,
                institution_name=institution_name,
                degree=degree,
                percentage=percentage,
                passed_out_year=passed_out_year,
                bank_name=bank_name,
                branch_name=branch_name,
                ifsc_code=ifsc_code,
                micr_code=micr_code,
                account_number=account_number,
                facebook_profile=facebook_profile,
                twitter_profile=twitter_profile,
                instagram_profile=instagram_profile,
                youtube_channel=youtube_channel,
                about_you=about_you,
                profile_photo=profile_photo,
                resume=resume,
                pan_card=pan_card,
                aadhar_card=aadhar_card,
                bank_passbook=bank_passbook,
                attribute1=None,
                attribute2=None,
                attribute3=None,
                attribute4=None,
                attribute5=None,
            )
            instructor.save()

        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")

    return render(request, 'Master/instructor.html')


def instructor_list(request):
    # Fetch all Instructor records from the database
    instructors = Instructor.objects.all()
    # Pass the data to the template
    return render(request, 'Master/instructor_list.html', {'instructors': instructors})

from .models import TeamCategory

# View to handle adding and deleting team categories
def team_category(request):
    if request.method == "POST":
        if "delete" in request.POST:
            # Handle deletion
            team_id = int(request.POST['delete'])
            try:
                team_category = TeamCategory.objects.get(id=team_id)
                team_category.delete()
                return redirect("team_category_master")  # Redirect after deletion
            except TeamCategory.DoesNotExist:
                return HttpResponse("Category not found", status=404)
        else:
            # Handle addition
            encrypted_data = request.POST.get("team_category")
            
            # You may decrypt the data here if needed before saving
            # Assuming no decryption for simplicity
            team_category = encrypted_data

            if team_category:
                new_team_category = TeamCategory(team_category=team_category)
                new_team_category.save()
                return redirect("team_category_master")
            return HttpResponse("Team category cannot be empty", status=400)

    # Fetch all team categories for display
    team_categories = TeamCategory.objects.all()
    return render(request, "Master/teamCategoryMaster.html", {"team_categories": team_categories})

def costcategory(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            # Handle delete
            try:
                category_id = request.POST.get('delete')
                category = CostCuttingCategoryMaster.objects.get(id=category_id)
                category.delete()
            except CostCuttingCategoryMaster.DoesNotExist:
                return HttpResponse("Category not found", status=404)
        else:
            # Handle form submission
            categroy_name = request.POST.get('category_name')
            category_image = request.FILES['category_image_box'].read()
        
            
            if categroy_name:
                CostCuttingCategoryMaster.objects.create(categroy_name=categroy_name,category_image=category_image)
            else:
                return HttpResponse("Invalid category name", status=400)

        return redirect('costcategory')

    # Fetch all categories for display
    categories = CostCuttingCategoryMaster.objects.all()
    return render(request, 'Master/costcategory.html', {'categroy_name': categories})

def daily(request):
    return render(request,'Master/form.html')

def weekly(request):
    return render(request,'Master/formw.html')

def common(request):
    return render(request,'Master/formc.html')


def bannerupload(request):
    return render(request,'Master/bannerform.html')

@csrf_exempt
def uploadbanner(request):
    file1 = request.FILES.get('file1')
    file2 = request.FILES.get('file2')
    file3 = request.FILES.get('file3')
    upload = bannerupload(banner1 = file1 , banner2 = file2 , banner3 = file3)
    upload.save()
    return JsonResponse({'success': 'yes'}, safe=False)

def view_students(request):
    # Fetch all records from the Student_Registration model
    students = ElearningRegistartion.objects.all()
    
    # Pass the data to your template
    return render(request, 'Master/view-students.html', {'students': students})

def view_startup(request):
    startups = StartupRegistartion.objects.all()
    return render(request, 'Master/view-startup.html', {'startups': startups})

def view_internship(request):
    intern = list(InternRegistartion.objects.filter(status='requested').values())
    context = {
    'interns':intern
        }
    return render(request, 'Master/view-students.html', context)

def accept_intern(request,pk):
   idn='IN161220246'
   data = InternRegistartion.objects.get(user_id=idn)
   data2 = Userauth.objects.get(user_id = idn)
   userid = data2.user_id
   passw = data2.password
   name = data.student_Name
   contact_email = data.contact_email
   data.status = 'accepted'
   data.save()
   subject = "Intern Registration Details"
   message = f"Dear {name},\n\nThank you for registering for our internship.\n\nYour User ID: {userid}\nYour Password: {passw}\n\nPlease keep this information secure.\n\nBest regards,\nIntern Registration Team"
   from_email = "sarveshsr@altruisty.in"
   recipient_list = [contact_email]
   send_mail(subject, message, from_email, recipient_list)
   return JsonResponse({'status':'success'})

def rejected_intern(request,pk):
   idn=pk
   data = InternRegistartion.objects.get(id=idn)
   data.status = 'rejected'
   data.save()
   return JsonResponse({'status':'success'})


@csrf_exempt
def uploaddq(request):
    qid=request.POST.get('qid')
    question=request.POST.get('question')
    si=request.POST.get('si')
    so=request.POST.get('so')
    ao=request.POST.get('ao')
    posted_on = str(datetime.now().date())
    data = dailyquestion(posted_on = posted_on , question_id=qid,question=question,sample_input=si,sample_output=so,actual_output = ao)
    data.save()
    return JsonResponse({'status':'success'})
    


@csrf_exempt
def uploadwq(request):
    qid=request.POST.get('qid')
    question=request.POST.get('question')
    si=request.POST.get('si')
    so=request.POST.get('so')
    ao=request.POST.get('ao')
    posted_on = str(datetime.now().date())
    data = weeklyquestion(posted_on = posted_on , question_id=qid,question=question,sample_input=si,sample_output=so,actual_output = ao)
    data.save()
    return JsonResponse({'status':'success'})

@csrf_exempt
def uploadcq(request):
    qid=request.POST.get('qid')
    question=request.POST.get('question')
    si=request.POST.get('si')
    so=request.POST.get('so')
    ao=request.POST.get('ao')
    posted_on = str(datetime.now().date())
    data = commonquestion(posted_on = posted_on , question_id=qid,question=question,sample_input=si,sample_output=so,actual_output = ao)
    data.save()
    return JsonResponse({'status':'success'})

def collegeList(request):
    colleges = collegeRegistartion.objects.all()
    return render(request,'Master/view-colleges.html',{'colleges':colleges})

def mentorList(request):
    mentors = MentorRegistartion.objects.all()
    return render(request,'Master/view-mentors.html',{'mentors':mentors})