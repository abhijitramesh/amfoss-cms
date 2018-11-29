from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^attendance/', attendance_api.as_view(), name='attendance_api'),
    url(r'^profile/', profile_api.as_view(), name='profile_api'),
    url(r'^responsibility/', responsibility_api.as_view(), name='responsibility_api')
]