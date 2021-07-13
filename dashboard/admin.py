from django.contrib import admin
from dashboard.models import Instruments

# Register your models here.
class InstrumentsAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Instruments, InstrumentsAdmin)