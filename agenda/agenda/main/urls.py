from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'agenda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',views.Home.as_view(),name="home"),
    url(r'^productos/$',views.Productos.as_view(),name="productos"),
]
