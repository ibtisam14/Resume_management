from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .swagger import swagger_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('resumeapp_account.urls')),
    path('api/', include('resumeapp.urls')),
]
urlpatterns += swagger_urlpatterns