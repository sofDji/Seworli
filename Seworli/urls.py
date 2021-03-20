from django.contrib import admin
from django.urls import path, include
from accounts.views import clients,photographes
from django.views.generic.base import TemplateView # new
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('Seworli_Shop.urls')),
	path('site/', include('accueil.urls')),
	path('accounts/', include('accounts.urls')), # new
	path('accounts/', include('django.contrib.auth.urls')),
	path('espace/', include('espaces_partage.urls')), # new
	path('notifications/', include('notify.urls', 'notifications')),
    path('messages/', include('postman.urls'),name='pos&tman'),

]
if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
