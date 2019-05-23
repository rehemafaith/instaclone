from django.conf.urls import url
from . import  views
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
  url('^$',views.home,name='home'),
  url('^profile/$',views.profile,name='profile'),
  url('^add/image$',views.add_image,name='add'),
  url('^update/$',views.update_profile,name='update')
]
if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)