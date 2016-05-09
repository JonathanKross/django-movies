from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^lensview/', include('lensview.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls'))
]
