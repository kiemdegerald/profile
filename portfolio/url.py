from django.urls import  path

from porte import settings
from django.conf.urls.static import static
from portfolio.views import contact_view, index


urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact_view, name='contact'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)