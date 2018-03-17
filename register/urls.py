from django.conf.urls import url,include
from register import views


urlpatterns = [
    url(r'^$', views.Adduser.as_view() , name='adduser'),
]

