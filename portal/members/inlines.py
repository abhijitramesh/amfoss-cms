from django.contrib import admin
from .models import *

class sp_inline(admin.TabularInline):
    model = SocialProfile
    extra = 0

class wexp_inline(admin.StackedInline):
    model = WorkExperience
    fields  = (('organization', 'position'), ('start', 'end'),'description',)
    extra = 0
