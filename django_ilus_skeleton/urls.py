"""django_ilus_skeleton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from two_factor.admin import AdminSiteOTPRequired
from django.conf import settings

from two_factor.urls import urlpatterns as tf_urls
from apps.pages.urls import urlpatterns as pages_urls
from core.users.urls import urlpatterns as users_urls


admin.site.__class__ = AdminSiteOTPRequired

urlpatterns = [
    path('', include(tf_urls)),
    path('', include('user_sessions.urls', 'user_sessions')),
    path('', include(pages_urls)),
    path('account/', include(users_urls)),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
