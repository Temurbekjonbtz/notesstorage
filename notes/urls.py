"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from django.views.static import  serve
from  django.conf.urls import  url

from .views import home_page, add, register_page, login_page, logout_page
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^home/$', home_page, name='home'),
    url(r'^$', register_page, name='register'),
    url(r'^login/$', login_page, name='login'),
    url(r'^add/$', add, name='add'),
    url(r'^logout/$', logout_page, name='logout'),
    url(r'^item/', include('item.urls')),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)