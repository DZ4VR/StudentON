# url(r'^login/$', views.login),
#     url(r'^logout/$', views.logout),
#     url(r'^register/$', views.register),


# url(r'^$', views.posts),
#     url(r'^(?P<article_id>\d+)$', views.post)

# url(r'^aboutus/', include('aboutPage.urls')),
#     url(r'^news/', include('newsPage.urls')),
#     url(r'^auth/', include('loginsys.urls')),

from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^aboutus/$',views.aboutPage),
    url(r'^news/$', views.posts),
    url(r'^news/(?P<article_id>\d+)$', views.post),
    url(r'^auth/logout/$', views.logout),
    url(r'^auth/login/$', views.login),
    url(r'^auth/register/$', views.register),
    url(r'^$', views.homePage),
]