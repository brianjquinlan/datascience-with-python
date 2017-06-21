from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex = r'^$',
        view = views.PostListView.as_view(),
        name = 'post_list'
    ),
    
    url(
        regex = r'^(?P<slug>[-\w]+)/$',
        view = views.PostDetailView.as_view(),
        name = 'post_detail'
    ),
]
