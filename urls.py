"""
URL configuration for CareerSpecs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from csweb.admin import *
from django.shortcuts import render

def custom_page_not_found(request):
    return render(request, "404.html")


handler404 = 'csweb.views.handler404'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("csweb.urls")),
    path("404/", custom_page_not_found),
]