"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from user.views import *
from distributor.views import *
urlpatterns = [
    path("api/get_announcements/<str:shop_id>/",get_announcements, name="get_announcements"),
    path("api/update_settings/", update_slot_settings, name="update_settings"),
    path("api/toggle_biometric/", toggle_biometric, name="toggle_biometric"),
    path("api/add_announcement/", add_announcement, name="add_announcement"),
    path("api/get_data/", get_distributor_data, name="get_distributor_data"),
    path('distributor_logout/',distributor_logout,name="distributor_logout"),
    path('distributor_dashboard',distributor_dashboard,name="distributor_dashboard"),
    path('distributor_login/',distributor_login,name="distributor_login"),
    path('distributor_register/',distributor_register,name="distributor_register"),
    path('logout/',logout_page,name="logout"),
    path('ekyc/',ekyc_page,name="ekyc"),
    path('register/',register_page,name="register"),
    path('dashboard/',dashboard_page,name="dashboard"),
    path('login/',login_page,name="login"),
    path('',home,name="home"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)