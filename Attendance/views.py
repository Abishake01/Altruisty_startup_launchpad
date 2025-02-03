from django.shortcuts import render
from django import forms
from .models import Student, Attendance

class AttendanceForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    student_name = forms.CharField(max_length=100)
    status = forms.ChoiceField(choices=[('Present', 'Present'), ('Absent', 'Absent')])

def attendance_list(request):
    attendance_data = Attendance.objects.all()
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['student_name']
            date = form.cleaned_data['date']
            status = form.cleaned_data['status'] == 'Present'

            student, created = Student.objects.get_or_create(name=student_name)
            Attendance.objects.create(student=student, date=date, is_present=status)

            form = AttendanceForm()  # Reset the form after submission
    else:
        form = AttendanceForm()

    context = {
        'form': form,
        'attendance_data': attendance_data,
    }
    return render(request, 'Attendance/attendance.html', context)
