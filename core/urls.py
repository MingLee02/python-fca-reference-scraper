from django.conf.urls import url
from django.contrib import admin

from .views import export, MainView, reference

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^reference/$', reference, name='post_ref'),
    url(r'^export/$', export, name='export'),
]
