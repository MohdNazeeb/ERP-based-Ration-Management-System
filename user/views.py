from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import get_user_model,authenticate,login,logout
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from distributor.models import *
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
User=get_user_model()

def home(request):
    return render(request,'index.html')

def logout_page(request):
    logout(request)
    return redirect('/')

def login_page(request):
    from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from distributor.models import Distributor
from .models import CustomUser

def login_page(request):
    if request.method == "POST":
        card_number = request.POST.get('card_number', '').strip()
        password = request.POST.get('password', '')

        if not CustomUser.objects.filter(card_number=card_number).exists():
            messages.error(request, "Invalid Card Number")
            return redirect('login')

        user = authenticate(request, card_number=card_number, password=password)

        if user is not None:
            login(request, user)
            shop_id = user.shop_id

            distributor = Distributor.objects.filter(shop_id=shop_id).first()
            distributor_name = distributor.full_name if distributor else "No Distributor Assigned"
            
            # ✅ Store for dashboard display
            # request.session['distributor_name'] = distributor_name
            # request.session['shop_id'] = shop_id
            # context={'distributor_name':distributor_name, 'shop_id':shop_id}
            return redirect('dashboard')

        else:
            messages.error(request, "Invalid Password")
            return redirect('login')

    return render(request, 'login.html')


@never_cache
@login_required(login_url='login')
def dashboard_page(request):
    user=request.user
    distributor=Distributor.objects.filter(shop_id=user.shop_id).first()
    distributor_name=distributor.full_name if distributor else "No distributor assigned"
    distributor_contact=distributor.mobile_number if distributor else "No distributor assigned"
    distributor_address=distributor.address if distributor else "No distributor assigned"
    context={'shop_id':user.shop_id,
            'distributor_name':distributor_name,
            'user':user,
            'distributor_contact' : distributor_contact,
            'distributor_address':distributor_address
            }
    return render(request,'dashboard.html',context=context)
        
def register_page(request):
    if request.method=="POST":
        card_type=request.POST.get('card_type')
        full_name=request.POST.get('full_name')
        card_number=request.POST.get('card_number')
        mobile_number=request.POST.get('mobile_number')
        shop_id=request.POST.get('shop_id')
        image=request.FILES.get('photo')
        password=request.POST.get('password')
        
        if CustomUser.objects.filter(card_number=card_number).exists():
            print(card_number)
            messages.error(request,"Card Number is already registered!")
            return redirect('register')
        user=CustomUser(
            card_type=card_type,
            full_name=full_name,
            card_number=card_number,
            mobile_number=mobile_number,
            shop_id=shop_id,
            image=image,
        )
        user.set_password(password)
        user.save()
        messages.success(request,"User registered succesfully")
        return redirect('/login/')
    return render(request,'register.html')

def ekyc_page(request):
    return render(request,'ekyc.html')


def get_distributor_data(request):
    user = request.user
    distributor = Distributor.objects.filter(shop_id=user.shop_id).first()

    settings = DistributorSettings.objects.filter(distributor=distributor).first()
    announcements = Announcement.objects.filter(distributor=distributor).order_by("-created_at")

    ann_list = [{"text": a.text, "created": a.created_at.strftime("%Y-%m-%d")} for a in announcements]

    return JsonResponse({
        "distribution_from": settings.distribution_from,
        "distribution_to": settings.distribution_to,
        "start_time": settings.start_time,
        "end_time": settings.end_time,
        "slot_limit": settings.slot_limit,
        "biometric_status": settings.biometric_status,
        "announcements": ann_list
    })
