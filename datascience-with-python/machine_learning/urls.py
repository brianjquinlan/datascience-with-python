from django.conf.urls import url

from . import views


urlpatterns = [
    
    url(
        regex = r'^$',
        view = views.main_page,
        name = 'main_page'
    ),

    url(
        regex = r'^numpy/$',
        view = views.numpy,
        name = 'numpy'
    ),

    url(
        regex = r'^pandas/$',
        view = views.pandas,
        name = 'pandas'
    ),

    url(
        regex = r'^scikitlearn/$',
        view = views.scikitlearn,
        name = 'scikitlearn'
    ),
]
