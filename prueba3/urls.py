from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('apAlo/',include('apAlo.urls')),
    path('', include('apAlo.urls')),
]
