from django.urls import path
from . import views

urlpatterns = [
    path('bannerform/',views.banner_upload,name="bannerform"),
    path('bannerlist/',views.banner_list,name="bannerlist"),
    path('homepage_uplod/',views.homeiamge_upload,name="homeimage_upload"),
    path('openimage_list/',views.homeimage_list,name="homeimage_list"),
    
]