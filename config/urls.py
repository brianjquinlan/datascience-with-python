"""datascience-with-python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from django.contrib import admin

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='site/homepage.html'), name='home'),
    url(r'^about$', TemplateView.as_view(template_name='site/about.html'), name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('datascience_with_python.blog.urls', namespace='blog')),
    url(r'^machine-learning/', include('datascience_with_python.machine_learning.urls', namespace='machine_learning')),
    url(r'^comments/', include('django_comments_xtd.urls')),
    
]

# setup django toolbar and static/media for development
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    # allows for serving files during development stage.  should not be used
    # in production
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
