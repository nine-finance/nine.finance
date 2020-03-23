from django.contrib import admin
from .models import post
from adminfiles.admin import FilePickerAdmin


class PostAdmin(FilePickerAdmin):
    adminfiles_fields = ('content',)


admin.site.register(post, PostAdmin)
