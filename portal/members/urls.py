from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    url(r'^api/attendance/', AttendanceList.as_view(), name='api_attendance')
]