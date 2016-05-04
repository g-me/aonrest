from django.conf.urls import include, url
from django.contrib import admin

from iapi.urls import router
urlpatterns = [
    # url(r'^api/token/', obtain_auth_token, name='api-token'),
    # url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),

]

