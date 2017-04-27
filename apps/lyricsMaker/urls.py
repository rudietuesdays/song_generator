from django.conf.urls import url
from views import Welcome, Songs, Library

app_name = 'lyricsMaker'

urlpatterns = [
    url(r'^$', Welcome.as_view(), name='index'),
    url(r'song$', Songs.as_view(), name='song'),
    url(r'library$', Library.as_view(), name='library'),
]
