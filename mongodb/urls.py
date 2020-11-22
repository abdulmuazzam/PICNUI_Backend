"""mongodb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from picnui.views import Add_Routine_API, Get_All_Routines_API
from picnui.subViews import *
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^routine/', Add_Routine_API, name='routine'),
    url(r'^AllRoutine/', Get_All_Routines_API, name='getRoutines'),

    url(r'^Testing/', Testing, name='Testing'),
    url(r'^RecoredVideo/', RecordedVideoEvent, name='RecoredVideo'),
    url(r'^KinectLiveStream/', KinectLiveStreamEvent, name='KinectLiveStream'),
    url(r'^CameraLiveStream/', CameraLiveStreamEvent, name='CameraLiveStream'),
    url(r'^CameraStaticImage/', CameraStaticImageEvent, name='CameraStaticImage'),
    url(r'^StaticImage/', StaticImageEvent, name='StaticImage'),


]


