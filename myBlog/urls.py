from django.conf.urls import url
from django.contrib import admin

from . import views as base_views

# importing app views (post)
from post import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  # ADMIN PAGE
                  url(r'^admin/', admin.site.urls),

                  # LANDING PAGE
                  url(r'^$', base_views.home),  # ROOT

                  # POST ROUTING
                  # note the use of exact match routing. If you dont use it, it will always find the /post patter, no matter what you are trying to do.
                  url(r'^post/$', views.index, name='post'),  # index form
                  url(r'^post/create/$', views.create, name='post_create')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
