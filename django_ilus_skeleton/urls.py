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
from django.urls import path, include, re_path
from two_factor.admin import AdminSiteOTPRequired
from django.conf import settings

from two_factor.urls import urlpatterns as tf_urls
from apps.pages.urls import urlpatterns as pages_urls
from core.users.urls import urlpatterns as users_urls

from django.contrib.sitemaps.views import sitemap
from apps.pages.sitemaps import PagesSitemap  # import StaticSitemap

sitemaps = {
    'static': PagesSitemap  # add StaticSitemap to the dictionary
}


admin.site.__class__ = AdminSiteOTPRequired


admin.site.site_header = 'Ilus skeleton'    # default: "Django Administration"
admin.site.index_title = 'Réglages généraux'    # default: "Site administration"
admin.site.site_title = 'iLus Skeleton'     # default: "Django site admin"

urlpatterns = [
    path('', include(tf_urls)),
    path('', include('user_sessions.urls', 'user_sessions')),
    path('', include(pages_urls)),
    path('account/', include(users_urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^robots\.txt', include('robots.urls')),

]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
