from django.http import HttpResponse
from django.shortcuts import render
from .models import Banner, HomeImage

# Create your views here.
def banner_uplod(request):
    if request.method == 'POST':
        try:
            banner1 = request.FILES['banner1'].read() if 'banner1' in request.FILES else None
            banner2 = request.FILES['banner2'].read() if 'banner2' in request.FILES else None
            banner3 = request.FILES['banner3'].read() if 'banner3' in request.FILES else None
            
            banner = Banner(
                banner1=banner1, 
                banner2=banner2, 
                banner3=banner3
                )
            banner.save()
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")
    return render(request, 'Master/bannerform.html')

def banner_list(request):
    # Fetch all Instructor records from the database
    banners = Banner.objects.all()
    # Pass the data to the template
    return render(request, 'Master/instructor_list.html', {'banners': banners})

