from django.urls import path
from .views import thong_ke_sinh_vien, thong_ke_thi

urlpatterns = [
    path('thong-ke-sv/', thong_ke_sinh_vien),
    path('thong-ke-thi/', thong_ke_thi),
]