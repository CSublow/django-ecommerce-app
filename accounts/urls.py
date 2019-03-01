from django.conf.urls import url, include
from accounts.views import index, logout, login, registration, user_profile
from accounts import url_reset

urlpatterns = [
    url(r'^logout/$', logout, name="logout"), # Setting the name means the logout can map to this url here (?)
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="registration"),
    url(r'^user-profile/$', user_profile, name="user-profile"),
    url(r'^password-reset/', include(url_reset))
]