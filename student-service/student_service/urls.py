"""
URL configuration for student_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from students.views import (
    KhoaViewSet, 
    NganhDaoTaoViewSet, 
    SinhVienViewSet,
    import_students,
    student_cdr_status   # <-- THÊM DÒNG NÀY
)  # thêm dòng này


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('students.urls')),
     path('api/import-students/', import_students, name='import_students'),
     # trong student_service/urls.py
    path('api/sinhvien/<int:student_id>/cdr-status/', student_cdr_status, name='student_cdr_status'),
]
