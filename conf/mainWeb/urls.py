from django.conf.urls import url
from . import views
from . import report_professor, ggul_tip_professor

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^labintro/$', views.lab_intro, name='Lab_intro'),
    url(r'^profeintro/$', views.profe_intro, name='Profe_intro'),
    url(r'^unknownpost/$', views.unknown_post, name='Unknown_post'),
    url(r'^unknownpostcreate/$', views.unknown_post_create, name='unknown_post_create'),
    url(r'^unknownpostdetail/(?P<pk>\d+)/$', views.unknown_post_detail, name='Unknown_post_detail'),
    url(r'^profeinfo/$', views.profe_info, name='Profe_info'),
    url(r'^ggultip/(?P<pr>\w+)/$', views.ggul_tip, name='GGul_tip'),
    url(r'^report/(?P<pr>\w+)/$', views.report, name='report'),
    url(r'^ggultip/details/(?P<pr>\w+)/(?P<pk>\d+)/$', views.ggulTipDetail, name='GGul_tip_detail'),
    url(r'^ggultip/create/angijung$', ggul_tip_professor.angijung_ggulTipCreate ,name="ggultip_create_angijung"),
    url(r'^ggultip/create/byunsangyong$', ggul_tip_professor.byunsangyong_ggulTipCreate ,name="ggultip_create_byunsangyong"),
    url(r'^ggultip/create/byunyoungchul$', ggul_tip_professor.byunyoungchul_ggulTipCreate ,name="ggultip_create_byunyoungchul"),
    url(r'^ggultip/create/gwakhoyoung$', ggul_tip_professor.gwakhoyoung_ggulTipCreate ,name="ggultip_create_gwakhoyoung"),
    url(r'^ggultip/create/kimdohyun$', ggul_tip_professor.kimdohyun_ggulTipCreate ,name="ggultip_create_kimdohyun"),
    url(r'^ggultip/create/leesangjun$', ggul_tip_professor.leesangjun_ggulTipCreate ,name="ggultip_create_leesangjun"),
    url(r'^ggultip/create/songwangchul$', ggul_tip_professor.songwangchul_ggulTipCreate ,name="ggultip_create_songwangchul"),
    url(r'^ggultip/create/kimjanghyung$', ggul_tip_professor.kimdohyun_ggulTipCreate ,name="ggultip_create_kimjangyung"),

    url(r'^report/create/angijung$', report_professor.angijung_reportCreate ,name="report_create_angijung"),
    url(r'^report/create/byunsangyong$', report_professor.byunsangyong_reportCreate ,name="report_create_byunsangyong"),
    url(r'^report/create/byunyoungchul$', report_professor.byunyoungchul_reportCreate ,name="report_create_byunyoungchul"),
    url(r'^report/create/gwakhoyoung$', report_professor.gwakhoyoung_reportCreate ,name="report_create_gwakhoyoung"),
    url(r'^report/create/kimdohyun$', report_professor.kimdohyun_reportCreate ,name="report_create_kimdohyun"),
    url(r'^report/create/leesangjun$', report_professor.leesangjun_reportCreate ,name="report_create_leesangjun"),
    url(r'^report/create/songwangchul$', report_professor.songwangchul_reportCreate ,name="report_create_songwangchul"),
    url(r'^report/create/kimjanghyung$', report_professor.kimjanghyung_reportCreate ,name="report_create_kimjangyung"),

    url(r'^jokbo/$', views.jokbo, name='jokbo'),
    url(r'^mypage/$', views.mypage, name='mypage'),
    url(r'^signup/$', views.signUp, name='signup'),
    url(r'^lab_member/$', views.lab_member, name='lab_member'),
    url(r'^message/$', views.message, name='message'),

]
