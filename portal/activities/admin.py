from django.contrib import admin
from .models import *
from easy_select2 import select2_modelform
from members.inlines import sp_inline

class workshop_details_inline(admin.StackedInline):
    model = workshop_details
    extra = 0

class project_details_inline(admin.StackedInline):
    model = project_details
    extra = 0
class project_links_inline(admin.TabularInline):
    model = project_links
    extra = 0


class workshopAdmin(admin.ModelAdmin):
    fields = (('name'), 'link', 'organizers',('skills','level'), ('start_date', 'end_date'),  ('seats', 'fee','poster'))
    inlines = (workshop_details_inline,)
    list_display = ('name', 'level', 'start_date', 'end_date')
    list_filter = ('level',)
    search_fields = ['level',]
    select2 = select2_modelform(workshop, attrs={'width': '250px'})
    form = select2

class projectAdmin(admin.ModelAdmin):
    inlines = (project_details_inline,project_links_inline)
    select2 = select2_modelform(workshop, attrs={'width': '250px'})
    form = select2

admin.site.register(workshop,workshopAdmin)
admin.site.register(project,projectAdmin)
