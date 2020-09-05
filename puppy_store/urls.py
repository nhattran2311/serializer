from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('puppies.urls')),
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    path('admin/', admin.site.urls),
]
#http://localhost:8000/api/v1/puppies