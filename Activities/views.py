from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question
from django.views.decorators.csrf import csrf_exempt
from Master.models import CostCuttingCategoryMaster

@csrf_exempt  # To handle CSRF token if testing with external tools
def add_costquestions(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            # Handle delete
            try:
                question_id = request.POST.get('delete')
                question = Question.objects.get(id=question_id)
                question.delete()
            except Question.DoesNotExist:
                return HttpResponse("Question not found", status=404)
        else:
            # Handle form submission
            category_name = request.POST.get('category')
            question_number = request.POST.get('question_number', 0)
            question = request.POST.get('question')

            # Options and associated fields
            option1 = request.POST.get('option1')
            efficiency_1 = request.POST.get('efficiency1', 0)
            description_1 = request.POST.get('justification1')

            option2 = request.POST.get('option2')
            efficiency_2 = request.POST.get('efficiency2', 0)
            description_2 = request.POST.get('justification2')

            option3 = request.POST.get('option3')
            efficiency_3 = request.POST.get('efficiency3', 0)
            description_3 = request.POST.get('justification3')

            option4 = request.POST.get('option4')
            efficiency_4 = request.POST.get('efficiency4', 0)
            description_4 = request.POST.get('justification4')
            correct_option = request.POST.get('correct_option')

            # Create a new Question object and save it to the database
            question_obj = Question(
                category_name=category_name,
                question_number=question_number,
                question=question,
                option1=option1,
                efficiency_1=efficiency_1,
                description_1=description_1,
                option2=option2,
                efficiency_2=efficiency_2,
                description_2=description_2,
                option3=option3,
                efficiency_3=efficiency_3,
                description_3=description_3,
                option4=option4,
                efficiency_4=efficiency_4,
                description_4=description_4,
                correct_option=correct_option,
            )
            question_obj.save()

        return redirect('costquestions')

    # Fetch existing categories for the dropdown
    category_list = CostCuttingCategoryMaster.objects.all()

    # Fetch all questions to display in the table
    categories = Question.objects.all()

    return render(request, 'Activities/add_costquestions.html', {
        'category_list': category_list,
        'categories': categories
    })