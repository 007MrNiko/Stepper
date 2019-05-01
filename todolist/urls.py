from django.urls import path, include
from django.contrib import admin

#connecting of urls
urlpatterns = [
    path('', include('lists.urls')),
    path('auth/', include('accounts.urls')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('weather/', include('weather.urls')),
    path('about/', include('about.urls')),
]
