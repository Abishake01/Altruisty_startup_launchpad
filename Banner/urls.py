from django.urls import path
from . import views

urlpatterns = [
    path('bannerform/',views.banner_uplod,name="bannerform"),
    path('bannerlist/',views.banner_list,name="bannerlist"),
    
]