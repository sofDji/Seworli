from django.contrib import admin
from .models import Drone, Appareil,Objectif,Accessoires

admin.site.register(Drone)
admin.site.register(Appareil)
admin.site.register(Objectif)
admin.site.register(Accessoires)
