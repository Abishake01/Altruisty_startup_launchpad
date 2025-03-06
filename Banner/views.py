import base64
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
 
from .models import Banner, HomeImage, Events_update
import traceback
import logging


logger = logging.getLogger(__name__)

def banner_upload(request):
    if request.method == 'POST':
       
        try:
            logger.info(f"Files received: {request.FILES}")

            # Get the file objects from request.FILES
            banner1 = request.FILES.get('file1')
            banner2 = request.FILES.get('file2')
            banner3 = request.FILES.get('file3')

            if not banner1 or not banner2 or not banner3:
                return JsonResponse({'status': 'error', 'message': 'All three banners are required.'}, status=400)

            # Create a new Banner instance with the binary data
            banner = Banner(
                banner1=banner1.read(),
                banner2=banner2.read(),
                banner3=banner3.read(),
            )
            banner.save()

            return JsonResponse({'status': 'success', 'message': 'Banners uploaded successfully!'})
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
    
# For debugging only - remove in production
def homeimage_upload(request):
    if request.method == 'POST':
         
        try:
            logger.info(f"Files received: {request.FILES}")

            college_home = request.FILES.get('college_home')
            intern_home = request.FILES.get('intern_home')
 
            if not college_home or not intern_home:
                missing = []
                if not college_home:
                    missing.append("college_home")
                if not intern_home:
                    missing.append("intern_home")
                    
                return JsonResponse({
                    'status': 'error', 
                    'message': f'Missing required images: {", ".join(missing)}'
                }, status=400)

            # Create a new HomeImage instance with the binary data
            home_image = HomeImage(
                college_home=college_home.read(),
                intern_home=intern_home.read()
            )
            home_image.save()
             
            return JsonResponse({'status': 'success', 'message': 'Home images uploaded successfully!'})
            
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
    
    
def events_upload(request):
    if request.method == 'POST':
         
        try:
            logger.info(f"Files received: {request.FILES}")

            event = request.FILES.get('events')
 
            if not event:
                return JsonResponse({'status': 'error', 'message': 'Event Image are Required'}, status=400)

            # Create a new Events_update instance with the binary data
            events_update = Events_update(
                events =event.read(),
               
            )
            events_update.save()
             
            return JsonResponse({'status': 'success', 'message': 'Event image uploaded successfully!'})
        except Exception as e:
            logger.error(f"Error in events_upload: {str(e)}")
            logger.error(traceback.format_exc())
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return render(request, 'Master/event_upload.html')


def eventuploaded_list(request):
    try:
        events_list = Events_update.objects.all()
        return render(request, 'Master/eventlist.html', {'events_list': events_list})
    except Exception as e:
        logger.error(f"Error in eventuploaded_list: {str(e)}")
        logger.error(traceback.format_exc())
        return HttpResponse(f"An error occurred: {e}")