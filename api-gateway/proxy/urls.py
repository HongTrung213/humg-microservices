from django.urls import re_path
from .views import ProxyView

urlpatterns = [
    re_path(r'^(?P<service>\w+)/(?P<path>.*)$', ProxyView.as_view(), name='proxy'),
]
