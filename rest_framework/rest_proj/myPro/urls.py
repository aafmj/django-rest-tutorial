"""myPro URL Configuration

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
from django.urls import path, include
from rest_framework.authtoken import views

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from user.urls import views as v

schema_view = get_schema_view(title="Example API")

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('myApp.urls')),  # 127.0.0.1:8000/func_name
    path('', v.profile),
    path('employee/', include('employee.urls')),  # 127.0.0.1:8000/employee/func_name
    path('car/', include('car.urls')),  # 127.0.0.1:8000/car/func_name

    path('api-token-auth', views.obtain_auth_token),
    path('api-auth', include('rest_framework.urls')),

    path('user/', include('user.urls')),


    path('schema/', schema_view),
    path('docs/', include_docs_urls(title='Bookings API'))
]
