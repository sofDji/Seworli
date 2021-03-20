from django.contrib import admin

from .models import Client, User,Entreprise,Photographe,Nb_visits

class ClientAdmin(admin.ModelAdmin):
   list_display   = ('first_name', 'last_name','email')
   list_filter    = ('last_name',)
   ordering       = ('last_name', )

class PhotographeAdmin(admin.ModelAdmin):
   list_display   = ('first_name', 'last_name','email')
   list_filter    = ('last_name',)
   ordering       = ('last_name', )

class EntrepriseAdmin(admin.ModelAdmin):
   list_display   = ('nom_entreprise', 'last_name','email')
   list_filter    = ('last_name',)
   ordering       = ('last_name', )

class UserAdmin(admin.ModelAdmin):
   list_display   = ('username','first_name','last_name', 'email','is_client','is_photographe','is_entreprise')
   list_filter    = ('last_name',)
   ordering       = ('last_name', )

admin.site.site_header = "Seworli Administration"
admin.site.register(Client,ClientAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Photographe,PhotographeAdmin)
admin.site.register(Entreprise,EntrepriseAdmin)
admin.site.register(Nb_visits)
