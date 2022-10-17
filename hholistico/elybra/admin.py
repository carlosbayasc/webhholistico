from django.contrib import admin
from .models import Elybra

# Register your models here.
class ElybraAdmin(admin.ModelAdmin):
    readonly_fields= ('created','updated')

admin.site.register(Elybra,ElybraAdmin)