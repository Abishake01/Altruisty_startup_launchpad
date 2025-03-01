from django.urls import path
from . import views

urlpatterns = [
    path('bannerform/', views.banner_upload, name="bannerform"),
    path('bannerlist/', views.banner_list, name="bannerlist"),
    path('uploadbanner/', views.banner_upload, name="uploadbanner"),
    path('homeimage_upload/', views.homeimage_upload, name="homeimage_upload"),
    path('homeimage_list/', views.homeimage_list, name="homeimage_list"),
]