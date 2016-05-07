from django.conf.urls import include, url
from django.contrib import admin

from iapi.urls import router
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]

