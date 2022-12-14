"""hotMops URL Configuration

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
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from decorator_include import decorator_include

admin.site.site_header = "hotMops Admin"
admin.site.site_title = "hotMops' Super Admin Portal"
admin.site.index_title = "Welcome to hotMops"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("userApp.urls")),
    path("home/", decorator_include(login_required, "main.urls")),
    path("common/", include("common.urls")),
]
