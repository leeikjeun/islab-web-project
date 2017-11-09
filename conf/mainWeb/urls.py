from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^labintro/$', views.lab_intro, name='Lab_intro'),
    url(r'^profeintro/$', views.profe_intro, name='Profe_intro'),
    url(r'^unknownpost/$', views.unknown_post, name='Unknown_post'),
    url(r'^unknownpostcreate/$', views.unknown_post_create, name='unknown_post_create'),
    url(r'^unknownpostdetail/(?P<pk>\d+)/$', views.unknown_post_detail, name='Unknown_post_detail'),
    url(r'^profeinfo/$', views.profe_info, name='Profe_info'),
    url(r'^ggultip/(?P<pr>\w+)/$', views.ggul_tip, name='GGul_tip'),
    # url(r'^ggultipdetail.html/$', views.ggul_tip_create, name='ggul_tip_create'),
    # url(r'^ggultip/$', views.GGul_tip, name='GGul_tip'),
    url(r'^jokbo/$', views.jokbo, name='jokbo'),
    url(r'^report/$', views.report, name='report'),
    url(r'^mypage/$', views.mypage, name='mypage'),
    url(r'^signup/$', views.signUp, name='signup'),
    url(r'^lab_member/$', views.lab_member, name='lab_member'),
    url(r'^message/$', views.message, name='message'),

]
