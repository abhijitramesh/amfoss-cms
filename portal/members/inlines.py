from django.contrib import admin
from .models import *

class sp_inline(admin.TabularInline):
    model = social_profiles
    extra = 0

class wexp_inline(admin.StackedInline):
    model = work_experiances
    fields  = (('organization', 'position'), ('start', 'end'),'description',)
    extra = 0
