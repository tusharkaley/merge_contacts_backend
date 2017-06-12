from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.add_user, name='add_user'),
    url(r'^usercontacts$', views.user_contacts, name='user_contacts'),
    url(r'^usercontacts/new$', views.new_contact, name='new_contact'),
    url(r'^usercontacts/mergecands$', views.merge_candidates, name='merge_candidates'),
    url(r'^trials$', views.trials, name='trials'),
]