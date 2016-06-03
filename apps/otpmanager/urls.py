from django.conf.urls import url

import views

urlpatterns = [
    url(r'^home/$',views.Index.as_view(), name='index'),
    url(r'^get_user_details/$', views.get_user_details, name="get_user_details"),
    url(r'^send-msg/$', views.SendMessage.as_view(), name="send_msg")

]