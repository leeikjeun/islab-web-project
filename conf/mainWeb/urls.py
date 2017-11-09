from django.conf.urls import url
from . import views
from . import professor

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^labintro0/$', views.lab_intro, name='Lab_intro'),
    url(r'^profeintro/$', views.profe_intro, name='Profe_intro'),
    url(r'^unknownpost/$', views.unknown_post, name='Unknown_post'),
    url(r'^unknownpostcreate/$', views.unknown_post_create, name='unknown_post_create'),
    url(r'^unknownpostdetail/(?P<pk>\d+)/$', views.unknown_post_detail, name='Unknown_post_detail'),
    url(r'^profeinfo/$', views.profe_info, name='Profe_info'),
    # url(r'^ggultip/(?P<pr>\w+)/$', views.ggul_tip, name='GGul_tip'),
    url(r'^ggultip/leesangjun/$', professor.lee_ggultip, name='lee_ggultip'),
    url(r'^report/leesangjun/$', professor.lee_report, name='lee_report'),
    url(r'^ggultip/angijung/$', professor.an_ggultip, name='an_ggultip'),
    url(r'^report/angijung/$', professor.an_report, name='an_report'),
    url(r'^ggultip/byunsangyong/$', professor.byun1_ggultip, name='byun1_ggultip'),
    url(r'^report/byunsangyong/$', professor.byun1_report, name='byun1_report'),
    url(r'^ggultip/byunyoungchul/$', professor.byun0_ggultip, name='byun0_ggultip'),
    url(r'^report/byunyoungchul/$', professor.byun0_report, name='byun0_report'),
    url(r'^ggultip/gwakhoyoung/$', professor.gwak_ggultip, name='gwak_ggultip'),
    url(r'^report/gwakhoyoung/$', professor.gwak_report, name='gwak_report'),
    url(r'^ggultip/kimdohyun/$', professor.kim0_ggultip, name='kim0_ggultip'),
    url(r'^report/kimdohyun/$', professor.kim0_report, name='kim0_report'),
    url(r'^ggultip/kimjanghyung/$', professor.kim1_ggultip, name='kim1_ggultip'),
    url(r'^report/kimjanghyung/$', professor.kim1_report, name='kim1_report'),
    url(r'^ggultip/songwangchul/$', professor.song_ggultip, name='song_ggultip'),
    url(r'^report/songwangchul/$', professor.song_report, name='song_report'),
    # url(r'^ggultipdetail.html/$', views.ggul_tip_create, name='ggul_tip_create'),
    # url(r'^ggultip/$', views.GGul_tip, name='GGul_tip'),
    url(r'^jokbo/$', views.jokbo, name='jokbo'),
    url(r'^report/$', views.report, name='report'),
    url(r'^mypage/$', views.mypage, name='mypage'),
    url(r'^signup/$', views.signUp, name='signup'),
    url(r'^lab_member/$', views.lab_member, name='lab_member'),
    url(r'^message/$', views.message, name='message'),

]
