from django.conf.urls import url

from drivers import views

urlpatterns = [
    url(r'^$', views.DriverList.as_view()),
    url(r'^(?P<pk>[0-9]+)$', views.DriverDetail.as_view())
]
