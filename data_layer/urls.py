from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from rest_app.views import DokarrsViewSet
router = routers.DefaultRouter()
router.register('dokarrs',DokarrsViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'data_layer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
