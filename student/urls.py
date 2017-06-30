from django.conf.urls import url
from . import views

app_name = 'student'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^register/$', views.RegisterView.as_view(), name='register')

]