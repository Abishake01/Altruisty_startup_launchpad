from django.urls import path
from . import views

urlpatterns = [
    path('events_upload/', views.events_upload, name="events_upload"),
    path('events_list/', views.eventuploaded_list, name="events_list"),   
    path('bannerlist/', views.banner_list, name="bannerlist"),
    path('uploadbanner/', views.banner_upload, name="uploadbanner"),
    path('homeimage_upload/', views.homeimage_upload, name="homeimage_upload"),
    path('homeimage_list/', views.homeimage_list, name="homeimage_list"),
]