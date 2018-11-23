from django.contrib import admin
from .models import *
from easy_select2 import select2_modelform


class categoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'parent')
    list_filter = ('parent',)
    select2 = select2_modelform(category, attrs={'width': '250px'})
    form = select2

class postAdmin(admin.ModelAdmin):
    fields  = ('title','author',('category', 'tags'),'content')
    list_display = ('title', 'author', 'category')
    list_filter = ('author','category','tags')
    search_fields = ['title', 'author', 'category', 'tags']
    select2 = select2_modelform(post, attrs={'width': '250px'})
    form = select2

admin.site.register(tag)
admin.site.register(category,categoryAdmin)
admin.site.register(post,postAdmin)
admin.site.register(external_post)