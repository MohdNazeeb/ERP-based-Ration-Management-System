from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Distributor, DistributorSettings, Announcement, BiometricStatus
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
CustomUser=get_user_model()
# Create your views here.
def distributor_logout(request):
    logout(request)
    return redirect('/')

def distributor_login(request):
    if request.method == "POST":
        license_number = request.POST.get('license_number')
        password = request.POST.get('password')
        # Authenticate using license_number as card_number
        user = authenticate(request, card_number=license_number, password=password)

        if user is not None:
            login(request, user)
            return redirect('distributor_dashboard')
        else:
            messages.error(request, "Invalid License Number or Password")
            return redirect('distributor_login')

    return render(request, 'distributor_login.html')

    
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Distributor

def distributor_register(request):
    if request.method == "POST":
        distributor_name = request.POST.get('name')
        shop_id = request.POST.get('shop_id')
        license_number = request.POST.get('license_number')
        shop_address = request.POST.get('shop_address')
        shop_photo = request.FILES.get('shop_photo')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Password mismatched!')
            return redirect('distributor_register')

        if Distributor.objects.filter(shop_id=shop_id).exists():
            messages.error(request, 'Shop ID already registered!')
            return redirect('distributor_register')

        if Distributor.objects.filter(license_number=license_number).exists():
            messages.error(request, 'License Number already registered!')
            return redirect('distributor_register')
        
        

        user = CustomUser.objects.create_user(
            card_number=license_number,
            password=password,
            full_name=distributor_name,
            mobile_number=mobile,
            card_type="Distributor",
            shop_id=shop_id      
        )
        
        Distributor.objects.create(
            user=user,
            full_name=distributor_name,
            shop_id=shop_id,
            shop_name=shop_id,
            shop_address=shop_address,
            license_number=license_number,
            address=shop_address,
            image=shop_photo,
            mobile_number=mobile,
            email=email
        )
        messages.success(request, 'Distributor registered successfully!')
        return redirect('distributor_login')  
    return render(request, 'distributor_register.html')

def distributor_dashboard(request):
    user=request.user
    context= {'user':user}
    return render(request,'distributor_dashboard.html',context=context)

# ------------------ API FIXES ------------------- #

@csrf_exempt
@login_required
def update_slot_settings(request):
    if request.method == "POST":
        data = json.loads(request.body)

        distributor = Distributor.objects.get(user=request.user)
        settings, created = DistributorSettings.objects.get_or_create(distributor=distributor)

        settings.distribution_from = data.get("distribution_from")
        settings.distribution_to = data.get("distribution_to")
        settings.start_time = data.get("start_time")
        settings.end_time = data.get("end_time")
        settings.slot_limit = data.get("slot_limit")
        settings.save()

        return JsonResponse({"status": "success"})


@csrf_exempt
@login_required
def toggle_biometric(request):
    distributor = Distributor.objects.get(user=request.user)
    settings, created = DistributorSettings.objects.get_or_create(distributor=distributor)

    settings.biometric_status = "INACTIVE" if settings.biometric_status == "ACTIVE" else "ACTIVE"
    settings.save()

    return JsonResponse({"status": settings.biometric_status})


@csrf_exempt
@login_required
def add_announcement(request):
    if request.method == "POST":
        distributor = Distributor.objects.get(user=request.user)
        data = json.loads(request.body)

        Announcement.objects.create(
            distributor=distributor,
            text=data.get("text")
        )

        return JsonResponse({"status": "added"})
    

@csrf_exempt
@login_required
def get_announcements(request, shop_id):
    try:
        distributor = Distributor.objects.get(shop_id=shop_id)
    except Distributor.DoesNotExist:
        return JsonResponse({"announcements": []})

    data = Announcement.objects.filter(distributor=distributor).order_by('-id')

    announcements = [
        {"id": a.id, "text": a.text}
        for a in data
    ]

    return JsonResponse({"announcements": announcements})


#Jatin ->
@csrf_exempt
def update_status(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        device_id = data.get("device_id")
        status = data.get("status")

        BiometricStatus.objects.update_or_create(
            device_id=device_id,
            defaults={"status": status}
        )

        return JsonResponse({"message": "Status updated", "status": status})
    
    return JsonResponse({"error": "Invalid request"}, status=400)


def get_status(request, device_id):
    try:
        bio = BiometricStatus.objects.get(device_id=device_id)
        return JsonResponse({
            "device_id": bio.device_id,
            "status": bio.status,
            "timestamp": bio.timestamp
        })
    except BiometricStatus.DoesNotExist:
        return JsonResponse({"error": "Device not found"},status=404)