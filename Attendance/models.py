from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField()

    def __str__(self):
        return f'{self.student.name} - {self.date} - {"Present" if self.is_present else "Absent"}'
