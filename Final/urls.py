from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppThatBeer.urls')),
    path('user/', include('UserThatBeer.urls')),
    path('mensajes/', include ('Mensajes.urls')),
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
