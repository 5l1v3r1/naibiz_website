
from django.conf.urls import url,include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('biz.urls')),
    url(r'^accounts/',include('registration.backends.default.urls')),
    
   
      
]
