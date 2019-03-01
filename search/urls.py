from django.conf.urls import url
# import the do_search view from views.py
from .views import do_search

urlpatterns = [
    url(r'^$', do_search, name="search")
]