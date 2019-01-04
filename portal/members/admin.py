from django.contrib import admin
from .models import *
from .inlines import *
from easy_select2 import select2_modelform


class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Details', {
            'fields': (('user', 'role'), ('email', 'phone'),
                       ('first_name', 'last_name'), ('roll_number', 'batch'))
        }),
        ('Additional Details', {
            'fields': (('avatar', 'birthday'), ('location', 'system_no'), 'bio')
        }),
        ('Interests & Expertise', {
            'fields': (('interests', 'expertise'),)
        }),

    )
    inlines = (sp_inline, wexp_inline)
    list_display = ('first_name', 'last_name', 'role', 'batch')
    list_filter = ('batch','role')
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'batch', 'role']
    select2 = select2_modelform(Profile, attrs={'width': '250px'})
    form = select2


class AttendanceAdmin(admin.ModelAdmin):
    fields  = ('member',('session_start', 'session_end'),)
    select2 = select2_modelform(Attendance, attrs={'width': '250px'})
    form = select2


class ResponsibilityAdmin(admin.ModelAdmin):
    search_fields = ['title', 'members']
    list_display = ('title', 'thread')
    list_filter = ('title','members')
    select2 = select2_modelform(Responsibility, attrs={'width': '250px'})
    form = select2


class TeamAdmin(admin.ModelAdmin):
    search_fields = ['name', 'members']
    list_display = ('name', 'Thread')
    list_filter = ('name', 'members')
    select2 = select2_modelform(Team, attrs={'width': '250px'})
    form = select2


class MentorGroupAdmin(admin.ModelAdmin):
    search_fields = ['mentor', 'mentees']
    list_display = ('mentor',)
    list_filter = ('mentor',)
    select2 = select2_modelform(MentorGroup, attrs={'width': '250px'})
    form = select2


class PortalAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False


class OrganizationAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False


class SkillAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Responsibility, ResponsibilityAdmin)
admin.site.register(MentorGroup, MentorGroupAdmin)
admin.site.register(Portal, PortalAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Skill, SkillAdmin)
