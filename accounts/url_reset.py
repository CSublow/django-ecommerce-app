from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url(r'^$', password_reset, {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'), # The base url    
    url(r'^done$', password_reset_done, name='password_reset_done'), # The done url
    # The next url contains a token that is generated for each specific user. It will be a unique url
    # The uidb64 is made up of numbers from 0-9, capital letters from A-Z, and lowercase letters from a-z
    # Then comes the token itself
    # This url is the kind of thing that would be usually sent in an email
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    url(r'^complete/$$', password_reset_complete, name='password_reset_complete')
]