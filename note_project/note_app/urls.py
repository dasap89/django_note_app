from django.conf.urls import url
from . views import NoteList


urlpatterns = [
    url(r'^$', NoteList.as_view(), name="index"),
    ]
