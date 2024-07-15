from django.contrib import admin
from cars.models import *

class CarsModelAdmin(admin.ModelAdmin):
    list_display = ['id','brand','color','liscense_no']

admin.site.register(Cars,CarsModelAdmin)

class SpaceModelAdmin(admin.ModelAdmin):
    list_display = ['id','space_box']

admin.site.register(Space,SpaceModelAdmin)

class ParkSlotModelAdmin(admin.ModelAdmin):
    list_display = ['id','car','space','date']

admin.site.register(ParkSlot,ParkSlotModelAdmin)