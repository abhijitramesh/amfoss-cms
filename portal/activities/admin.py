from django.contrib import admin
from .models import *
from easy_select2 import select2_modelform
from members.inlines import sp_inline


class WorkshopDetailInline(admin.StackedInline):
    model = WorkshopDetail
    extra = 0


class ProjectDetailInline(admin.StackedInline):
    model = ProjectDetail
    extra = 0


class ProjectLinkInline(admin.TabularInline):
    model = ProjectLink
    extra = 0


class WorkshopAdmin(admin.ModelAdmin):
    fields = ('name', 'link', 'organizers', ('skills', 'level'), ('start_date', 'end_date'),  ('seats', 'fee', 'poster'))
    inlines = (WorkshopDetailInline,)
    list_display = ('name', 'level', 'start_date', 'end_date')
    list_filter = ('level',)
    search_fields = ['level']
    select2 = select2_modelform(Workshop, attrs={'width': '250px'})
    form = select2


class ProjectAdmin(admin.ModelAdmin):
    inlines = (ProjectDetailInline, ProjectLinkInline)
    select2 = select2_modelform(Workshop, attrs={'width': '250px'})
    form = select2

admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Project, ProjectAdmin)
