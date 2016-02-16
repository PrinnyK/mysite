from django.conf.urls import url
from .views import articleListView, articleDetailView

urlpatterns = [
	url(r'^$', articleListView.as_view(), name='home'),
	url(r'^article/(?P<pk>[0-9]+)/$', articleDetailView.as_view(), name='detail'),
	url(r'^category/(?P<pk>[0-9]+)/$', articleListView.as_view(), name='category'),
]
