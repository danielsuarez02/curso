from django.conf.urls import  url
from . import views 

urlpatterns = [
    # Examples:
    # url(r'^$', 'agenda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^foro$',views.Foro.as_view(),name="foro"),
    url(r'^foro/posts/$',views.Posts.as_view(),name="posts"),
    url(r'^foro/form/$',views.Form.as_view(),name="form"),
    url(r'^foro/listado/$',views.Listado.as_view(),name="listado"),
]
