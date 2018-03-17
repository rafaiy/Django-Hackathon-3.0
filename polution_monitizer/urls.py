from django.conf.urls import url,include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', include('register.urls')),
    url(r'^login', include('login.urls'), name='login'),
    url(r'^', include('Home.urls'))
]
