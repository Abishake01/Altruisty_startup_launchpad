from django.urls import path
from . import views



urlpatterns = [
    path('idea-submissions/',views.ideaSubmissions,name="idea_submissions"),
    path('statement_showcase_form/',views.statementshowcaseform,name="statement_showcase"),
    path('statement_showcase_form_category/',views.statementshowcasecategoryform,name="statement_showcase_category"),
    path('api/uploadstatementshowcase/',views.uploadstatementshow),
    path('api/uploadstatementshowcasecategory/',views.uploadstatementshowcategory),
    
]