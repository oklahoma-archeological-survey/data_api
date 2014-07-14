from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from dokarrs_app.views import DokarrsViewSet
from oas_doe.views import DoeViewSet
from views import APIRoot

router = routers.SimpleRouter()
#router.register('dokarrs', DokarrsViewSet)
router.register('doe',  DoeViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'data_layer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', APIRoot.as_view()),
)
