from rest_framework.views import APIView
from django.contrib.auth.models import User
from members.models import *
from members.serializer import *
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from datetime import datetime

class attendance_api(APIView):
    renderer_classes = (JSONRenderer, )
    permission_classes = (IsAdminUser,)

    def get(self, request):
        queryset = attendance.objects.all()

        username = self.request.query_params.get('username', None)
        date = self.request.query_params.get('date',None)
        year = self.request.query_params.get('year',None)
        month = self.request.query_params.get('month',None)
        batch = self.request.query_params.get('batch',None)

        if username is not None:
            user_obj = User.objects.filter(username=username)
            queryset = queryset.filter(member__in=user_obj)

            serializer = UserAttendanceSerializer(queryset,many=True)

        elif date is not None:
            datestamp = datetime.strptime(date, "%d%m%Y").date()
            queryset = queryset.filter(session_start__date=datestamp)
            serializer = DateAttendanceSerializer(queryset,many=True)

        else:
            if batch is not None:
                members = User.objects.filter(profile__batch=batch)
                queryset = queryset.filter(member__in=members)
            if year is not None:
                queryset = queryset.filter(session_start__year =year)
            if month is not None:
                queryset = queryset.filter(session_start__month=month)

            serializer = AttendanceSerializer(queryset,many=True)

        return Response(serializer.data)

class profile_api(APIView):
    renderer_classes = (JSONRenderer, )
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        queryset = profile.objects.all()

        username = self.request.query_params.get('username', None)
        birth_year = self.request.query_params.get('birth_year', None)
        birth_month = self.request.query_params.get('birth_month', None)
        interest = self.request.query_params.get('interested_in', None)
        expertise = self.request.query_params.get('expert_in', None)
        location = self.request.query_params.get('location', None)


        if username is not None:
            user_obj = User.objects.filter(username=username)
            queryset = queryset.filter(user__in=user_obj)

        if birth_year is not None:
            queryset = queryset.filter(birthday__year=birth_year)

        if birth_month is not None:
            queryset = queryset.filter(birthday__month=birth_month)

        if interest is not None:
            queryset = queryset.filter(interests__name__iexact=interest)

        if expertise is not None:
            queryset = queryset.filter(expertise__name__iexact=expertise)

        if location is not None:
            queryset = queryset.filter(location__icontains=location)

        serializer = ProfileSerializer(queryset, many=True)

        return Response(serializer.data)

class responsibility_api(APIView):
    renderer_classes = (JSONRenderer, )
    permission_classes = (IsAdminUser,)

    def get(self, request):
        queryset = responsibility.objects.all()

        username = self.request.query_params.get('username', None)

        if username is not None:
            user_obj = User.objects.filter(username=username)
            queryset = queryset.filter(members__in=user_obj)
            serializer = UserResponsibilitySerializer(queryset, many=True)
        else:
            serializer = ResponsibilitySerializer(queryset, many=True)

        return Response(serializer.data)

