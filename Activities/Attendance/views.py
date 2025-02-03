from django.shortcuts import render
from django import forms

# Define the form for manual attendance
class AttendanceForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    student_name = forms.CharField(max_length=100)
    status = forms.ChoiceField(choices=[('Present', 'Present'), ('Absent', 'Absent')])

def attendance_list(request):
    attendance_data = []
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            # Collect attendance data from the form
            attendance_record = {
                'date': form.cleaned_data['date'],
                'student_name': form.cleaned_data['student_name'],
                'status': form.cleaned_data['status']
            }
            attendance_data.append(attendance_record)
            form = AttendanceForm()  # Reset the form after submission
    else:
        form = AttendanceForm()

    context = {
        'form': form,
        'attendance_data': attendance_data,
    }
    return render(request, 'Attendance/attendance.html', context)
