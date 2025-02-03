from django.db import models

class Question(models.Model):
    category_name = models.CharField(max_length=255, default='General')
    question_number = models.IntegerField(default=1)
    question = models.TextField(default='')

    # Option 1
    option1 = models.TextField(default='')
    efficiency_1 = models.IntegerField(default=0)
    description_1 = models.TextField(default='')

    # Option 2
    option2 = models.TextField(default='')
    efficiency_2 = models.IntegerField(default=0)
    description_2 = models.TextField(default='')

    # Option 3
    option3 = models.TextField(default='')
    efficiency_3 = models.IntegerField(default=0)
    description_3 = models.TextField(default='')

    # Option 4
    option4 = models.TextField(default='')
    efficiency_4 = models.IntegerField(default=0)
    description_4 = models.TextField(default='')

    correct_option = models.CharField(max_length=255, default='')
   

    def __str__(self):
        return f"{self.category_name} - Question {self.question_number}"

    class Meta:
        db_table = 'costcuttingquestions'
