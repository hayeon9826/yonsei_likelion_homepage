from django.conf.urls import url 
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings
  
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^about/$',views.about, name='about'),
    url(r'^post/', views.post, name='post'),
    url(r'^(?P<pk>\d+)/$', views.post_detail),
    url(r'^(?P<pk>\d+)/comments/new/$', views.comment_new),
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.comment_edit)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)