from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = {
    # url(r'^alpha/auth/device_sign_in/$', auth.DeviceSignIn.as_view()),
    #
    # url(r'^alpha/user/register_couple/$', user.RegisterCouple.as_view()),
    # url(r'^alpha/user/is_couple/$', user.IsCouple.as_view()),
    #
    # url(r'^alpha/file/upload_file/$', file.UploadFile.as_view()),
    url(r'^$', views.index, name='index'),
    url(r'^thread/$', views.thread, name='thread'),
    #######
    url(r'^showmembers/$',views.members_list, name='members'),
    #######
}

urlpatterns = format_suffix_patterns(urlpatterns)
