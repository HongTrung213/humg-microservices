from django.urls import path
from .views import AssignRoleView

urlpatterns = [
    path('assign-role/', AssignRoleView.as_view(), name='assign_role'),
]