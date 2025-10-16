"""
URL configuration for python_apps_django project.

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

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("work05/", include("work05.urls")),
    path("work05_1/", include("work05_1.urls")),
    # path('work05_2/', include('work05_2.urls')),
    path("work06/", include("work06.urls")),
    path("work07/", include("work07.urls")),
    path("work08/", include("work08.urls")),
]
