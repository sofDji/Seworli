from django.contrib import admin
from .models import Project
admin.site.site_header = "Seworli Administration"


admin.site.register(Project)
