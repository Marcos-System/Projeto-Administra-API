from django.urls import path
from site_administrativo.views import *
from django.conf.urls.static import static
from django.conf import settings
app_name = 'site_administrativo'

urlpatterns = [
    path('', home, name='home'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)