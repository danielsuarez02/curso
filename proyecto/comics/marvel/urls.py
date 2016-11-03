from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.Home.as_view(),name="home"),
	url(r'^historial/',views.Historial.as_view(),name="historial"),
]