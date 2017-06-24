from django.conf.urls import url

from . import views
from .feeds import LatestPostsFeed

urlpatterns = [
    url(
        regex = r'^$',
        view = views.PostListView.as_view(),
        name = 'post_list'
    ),
    
    url(
        regex = r'^feed/$',
        view = LatestPostsFeed(),
        name = 'feed'
    ),

    url(
        regex = r'^archive/$',
        view = views.ArchiveIndexView.as_view(),
        name = 'archive_list'
    ),

    url(
        regex = r'^(?P<slug>[-\w]+)/$',
        view = views.PostDetailView.as_view(),
        name = 'post_detail'
    ),
    
    url(
        regex = r'^(?P<year>[0-9]{4})/(?P<month>[-\w]+)/$',
        view = views.MonthlyArchiveView.as_view(),
        name = 'archive_month'
    ),
]
