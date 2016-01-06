from django.conf.urls import url
from .views import articleListView, articleDetailView

urlpatterns = [
	url(r'^$', articleListView.as_view(), name='home'),
	url(r'^(?P<pk>[0-9]+)/$', articleDetailView.as_view(), name='detail')
]
