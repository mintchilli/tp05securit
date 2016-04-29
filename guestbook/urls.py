from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': 'post_list'}),
    url(r'^$', login_required(views.post_list), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', login_required(views.post_detail), name='post_detail'),
    url(r'^post/new/$', login_required(views.post_new), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', login_required(views.post_edit), name='post_edit'),
]
