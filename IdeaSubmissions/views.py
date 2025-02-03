from unicodedata import category
from django.http import JsonResponse
from django.shortcuts import render
from .models import statementshowcasecategoryform as sscf
from .models import statementshowcaseform as ssf
from .models import IdeaSubmission
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def ideaSubmissions(request):
    idea = list(IdeaSubmission.objects.all().values())
    statement = []
    for i in range(len(idea)):
        ps=ssf.objects.get(statement_id=idea[i]['statement_id'])
        statement.append(ps.statement)
    for i in range(len(idea)):
        idea[i]['statement_id']=statement[i]
  
    print(statement)
    context={
        'idea':idea
        }
    return render(request,'IdeaSubmission/IdeaSubmission.html',context)

def statementshowcaseform(request):
    category = list(sscf.objects.filter().values())
    context = {
        'category_list':category
        }
    return render(request, 'IdeaSubmission/statementshowcaseform.html',context)

def statementshowcasecategoryform(request):
    return render(request, 'IdeaSubmission/statementshowcasecategoryform.html')

@csrf_exempt
def uploadstatementshowcategory(request):
    categoryd = request.POST.get('category')
    data = sscf(statementcategory=categoryd)
    data.save()
    return JsonResponse({'status':'success'})

@csrf_exempt
def uploadstatementshow(request):
    statement_id = request.POST.get('statementid')
    statement = request.POST.get('statement')
    categoryd = request.POST.get('category')
    data = ssf(statement_id = statement_id,statement=statement,statementcategory=categoryd)
    data.save()
    return JsonResponse({'status':'success'})
