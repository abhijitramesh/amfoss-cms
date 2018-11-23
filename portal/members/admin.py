from django.contrib import admin
from .models import *
from .inlines import *
from easy_select2 import select2_modelform


class profileAdmin(admin.ModelAdmin):
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
    inlines = (sp_inline,wexp_inline)
    list_display = ('first_name', 'last_name', 'role', 'batch')
    list_filter = ('batch','role')
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'batch', 'role']
    select2 = select2_modelform(profile, attrs={'width': '250px'})
    form = select2


class attendanceAdmin(admin.ModelAdmin):
    fields  = ('member',('session_start', 'session_end'),)
    select2 = select2_modelform(attendance, attrs={'width': '250px'})
    form = select2

class responsibilityAdmin(admin.ModelAdmin):
    search_fields = ['title', 'members']
    list_display = ('title', 'thread')
    list_filter = ('title','members')
    select2 = select2_modelform(responsibility, attrs={'width': '250px'})
    form = select2

class teamAdmin(admin.ModelAdmin):
    search_fields = ['name', 'members']
    list_display = ('name', 'thread')
    list_filter = ('name','members')
    select2 = select2_modelform(team, attrs={'width': '250px'})
    form = select2

class mentor_groupAdmin(admin.ModelAdmin):
    search_fields = ['mentor', 'mentees']
    list_display = ('mentor',)
    list_filter = ('mentor',)
    select2 = select2_modelform(mentor_group, attrs={'width': '250px'})
    form = select2

class portalAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

class organizationAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

class skillAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False


admin.site.register(profile,profileAdmin)
admin.site.register(attendance,attendanceAdmin)
admin.site.register(team,teamAdmin)
admin.site.register(responsibility,responsibilityAdmin)
admin.site.register(mentor_group,mentor_groupAdmin)
admin.site.register(portal,portalAdmin)
admin.site.register(organization,organizationAdmin)
admin.site.register(skill,skillAdmin)
