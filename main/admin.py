from django.contrib import admin
from .models import UploadImage

class UploadImageAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
# Register your models here.
admin.site.register(UploadImage,UploadImageAdmin)