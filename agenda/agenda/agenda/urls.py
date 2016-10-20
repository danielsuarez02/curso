from django.conf.urls import include, url
from django.contrib import admin
from main import urls as main_view
from foro import urls as foro_view

urlpatterns = [
    # Examples:
    # url(r'^$', 'agenda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include(foro_view)),
    url(r'^',include(main_view)),
]
