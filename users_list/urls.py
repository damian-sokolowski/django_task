from django.conf.urls import url
from users_list.views import (
    IndexView, UserView, CreateUserView,
    UpdateUserView, DeleteUserView,
)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index',),
    url(
        r'^user/(?P<pk>[0-9]+)/$',
        UserView.as_view(),
        name='user_details',
    ),
    url(
        r'^user/add/$',
        CreateUserView.as_view(),
        name='add_user',
    ),
    url(
        r'^user/(?P<pk>[0-9]+)/edit/$',
        UpdateUserView.as_view(),
        name='edit_user',
    ),
    url(
        r'^user/(?P<pk>[0-9]+)/delete/$',
        DeleteUserView.as_view(),
        name='delete_user',
    ),
]
