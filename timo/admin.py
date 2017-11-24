from django.contrib import admin

# Register your models here.
from django.contrib import admin
from timo.models import Drivers
from timo.models import Run

class DriversAdmin(admin.ModelAdmin):
    pass
admin.site.register(Drivers, DriversAdmin)

class RunAdmin(admin.ModelAdmin):
    pass
admin.site.register(Run, RunAdmin)


