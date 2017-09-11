from django.conf.urls import url
from django.contrib import admin

from .views import MainView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MainView.as_view(), name='main'),
]
