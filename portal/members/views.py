from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from activities.models import *
from django.views.generic import View, ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from rest_framework import generics
from .serializer import AttendanceSerializer
from rest_framework.permissions import IsAdminUser


class AttendanceList(generics.ListCreateAPIView):
    queryset = attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = (IsAdminUser,)
