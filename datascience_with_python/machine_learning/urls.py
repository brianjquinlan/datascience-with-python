from django.conf.urls import url

from . import views


urlpatterns = [
    
    url(
        regex = r'^$',
        view = views.main_page,
        name = 'main_page'
    ),

    url(
        regex = r'^interactive/(?P<library>[-\w]+)/$',
        view = views.interactive,
        name = 'interactive'
    ),

    url(
        regex = r'^algorithms/$',
        view = views.algorithms,
        name = 'algorithms'
    ),

    url(
        regex = r'^libraries/$',
        view = views.libraries,
        name = 'libraries'
    ),
]
