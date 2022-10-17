from django.contrib import admin
from .models import Hipnoterapia

# Register your models here.
class HipnoterapiaAdmin(admin.ModelAdmin):
    readonly_fields= ('created','updated')

admin.site.register(Hipnoterapia,HipnoterapiaAdmin)