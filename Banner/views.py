from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Banner, HomeImage
import traceback
import logging

logger = logging.getLogger(__name__)

 
def banner_upload(request):
    if request.method == 'POST':
        try:
            logger.info(f"Files received: {request.FILES}")
            
            banner1 = request.FILES.get('file1').read() if 'file1' in request.FILES else None
            banner2 = request.FILES.get('file2').read() if 'file2' in request.FILES else None
            banner3 = request.FILES.get('file3').read() if 'file3' in request.FILES else None
            
            banner = Banner(
                banner1=banner1, 
                banner2=banner2, 
                banner3=banner3
            )
            banner.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            logger.error(f"Error in banner_upload: {str(e)}")
            logger.error(traceback.format_exc())
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return render(request, 'Master/bannerform.html')

def banner_list(request):
    try:
        banners = Banner.objects.all()
        return render(request, 'Master/bannerlist.html', {'banners': banners})
    except Exception as e:
        logger.error(f"Error in banner_list: {str(e)}")
        logger.error(traceback.format_exc())
        return HttpResponse(f"An error occurred: {e}")

@csrf_exempt  # For debugging only - remove in production
def homeimage_upload(request):
    if request.method == 'POST':
        try:
            logger.info(f"Files received: {request.FILES}")
            
            college_home = request.FILES.get('college_home').read() if 'college_home' in request.FILES else None
            intern_home = request.FILES.get('intern_home').read() if 'intern_home' in request.FILES else None
            
            home_image = HomeImage(
                intern_home=intern_home,
                college_home=college_home
            )
            home_image.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            logger.error(f"Error in homeimage_upload: {str(e)}")
            logger.error(traceback.format_exc())
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return render(request, 'Master/openimage.html')

def homeimage_list(request):
    try:
        open_images = HomeImage.objects.all()
        return render(request, 'Master/openimage_list.html', {'open_images': open_images})
    except Exception as e:
        logger.error(f"Error in homeimage_list: {str(e)}")
        logger.error(traceback.format_exc())
        return HttpResponse(f"An error occurred: {e}")